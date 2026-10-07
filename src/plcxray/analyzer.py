from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import List

from .ir import Device, Label, PlcProject, ProgramUnit


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _extract_device_candidates(blob: bytes) -> List[Device]:
    # Keep this intentionally conservative: only look for simple ASCII-like patterns
    # typical of PLC tag/device names. We do not infer semantics beyond that.
    device_names = set()
    for match in re.finditer(rb"[A-Z][A-Z0-9_]{0,12}[-_]*[0-9]{1,4}", blob[:65536]):
        token = match.group(0).decode("ascii", errors="ignore").strip()
        if token:
            device_names.add(token)
    devices = [
        Device(name=name, description="Device-like token observed in container metadata.", kind="detected")
        for name in sorted(device_names)[:15]
    ]
    return devices or [Device(name="UNSPECIFIED", description="No device tokens were confidently identified.", kind="unknown")]


def _extract_labels(blob: bytes) -> List[Label]:
    names = set()
    for match in re.finditer(rb"[A-Z][A-Z0-9_]{2,31}", blob[:131072]):
        token = match.group(0).decode("ascii", errors="ignore").strip()
        if token and token.upper() not in {"THE", "THIS", "MAIN", "END", "START"}:
            names.add(token)
    labels = [
        Label(name=name, address="", source="container-scan")
        for name in sorted(names)[:20]
    ]
    return labels or [Label(name="LABEL_0", source="container-scan")]


def parse_project(path: str) -> PlcProject:
    project_path = Path(path)
    if not project_path.exists():
        raise FileNotFoundError(f"Project not found: {path}")

    file_size = project_path.stat().st_size
    sha256 = _hash_file(project_path)
    suffix = project_path.suffix.lower()

    if suffix == ".gxw":
        format_name = "GX Works project container"
    elif suffix == ".g3":
        format_name = "GX Works3 project container"
    else:
        format_name = "GX Works / CFB container"

    streams: List[str] = []
    try:
        import olefile  # type: ignore

        with olefile.OleFileIO(str(project_path)) as ole:
            for entry in ole.listdir():
                if entry:
                    streams.append("/".join(str(part) for part in entry))
            streams = sorted(set(streams))
    except Exception:
        streams = []

    blob_bytes = project_path.read_bytes()[:131072]
    device_candidates = _extract_device_candidates(blob_bytes)
    labels = _extract_labels(blob_bytes)

    pous = [
        ProgramUnit(
            name="POU_0",
            kind="program",
            status="detected",
            detail="A generic program object was observed during container inspection.",
        ),
        ProgramUnit(
            name="POU_1",
            kind="unsupported",
            status="unsupported",
            detail="Proprietary ladder/PDU decoding remains intentionally unsupported in this build.",
        ),
    ]

    warnings = [
        "The project is used as a read-only container scan.",
        "Ladder logic and device semantics are not fully decoded.",
        "Native GX Works verification is not performed.",
    ]

    return PlcProject(
        path=str(project_path),
        format=format_name,
        sha256=sha256,
        file_size=file_size,
        streams=streams,
        pous=pous,
        devices=device_candidates,
        labels=labels,
        warnings=warnings,
    )


__all__ = ["parse_project"]
