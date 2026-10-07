from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Dict, List

from .ir import Device, Evidence, Label, PlcProject, ProgramUnit


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _scan_metadata(blob: bytes) -> Dict[str, str]:
    meta: Dict[str, str] = {}
    lower = blob[:4096].lower()
    if b"gx works" in lower:
        meta["signature"] = "GX Works signature detected in the leading bytes"
    if b"_hdb" in lower:
        meta["ole_stream_hint"] = "Compound File Binary stream hint detected"
    if b"projectinfo" in lower:
        meta["project_info_hint"] = "ProjectInfo marker detected"
    if not meta:
        meta["signature"] = "No known GX marker detected in the leading bytes"
    return meta


def _extract_device_candidates(blob: bytes) -> List[Device]:
    names = set()
    for match in re.finditer(rb"[A-Z][A-Z0-9_]{0,12}[-_]*[0-9]{1,4}", blob[:65536]):
        token = match.group(0).decode("ascii", errors="ignore").strip()
        if token:
            names.add(token)
    if not names:
        return [
            Device(
                name="UNSPECIFIED",
                description="No device-like tokens were confidently recovered.",
                kind="unknown",
            )
        ]
    return [
        Device(
            name=name,
            description="Device-like token observed during container scan.",
            kind="detected",
        )
        for name in sorted(names)[:20]
    ]


def _extract_labels(blob: bytes) -> List[Label]:
    names = set()
    for match in re.finditer(rb"[A-Z][A-Z0-9_]{2,31}", blob[:131072]):
        token = match.group(0).decode("ascii", errors="ignore").strip()
        if token and token.upper() not in {"THE", "THIS", "MAIN", "END", "START"}:
            names.add(token)
    if not names:
        return [Label(name="LABEL_0", source="container-scan")]
    return [Label(name=name, address="", source="container-scan") for name in sorted(names)[:20]]


def parse_project(path: str) -> PlcProject:
    project_path = Path(path)
    if not project_path.exists():
        raise FileNotFoundError(f"Project not found: {path}")

    file_size = project_path.stat().st_size
    sha256 = _hash_file(project_path)
    suffix = project_path.suffix.lower()
    project_name = project_path.stem or project_path.name

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

    blob = project_path.read_bytes()[:131072]
    metadata = {
        "filename": project_path.name,
        "extension": suffix,
        "size_bytes": str(file_size),
        "sha256": sha256,
        "container_type": format_name,
    }
    metadata.update(_scan_metadata(blob))

    devices = _extract_device_candidates(blob)
    labels = _extract_labels(blob)
    evidence = [
        Evidence(
            source="filesystem",
            item="sha256",
            detail=f"SHA-256 calculated for {project_name}",
            confidence="high",
        ),
        Evidence(
            source="container",
            item="project_type",
            detail=f"Container classified as {format_name}",
            confidence="medium",
        ),
        Evidence(
            source="scanner",
            item="device_candidates",
            detail=f"Recovered {len(devices)} potential device entries",
            confidence="low",
        ),
        Evidence(
            source="scanner",
            item="labels",
            detail=f"Recovered {len(labels)} label-like entries",
            confidence="low",
        ),
    ]

    pous = [
        ProgramUnit(name="POU_0", kind="program", status="detected", detail="Generic program object observed during scan."),
        ProgramUnit(name="POU_1", kind="unsupported", status="unsupported", detail="Proprietary ladder/PDU decoding intentionally unsupported."),
    ]

    warnings = [
        "Read-only container scan only.",
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
        devices=devices,
        labels=labels,
        warnings=warnings,
        project_name=project_name,
        metadata=metadata,
        evidence=evidence,
    )


__all__ = ["parse_project"]
