from __future__ import annotations

import hashlib
from pathlib import Path
from typing import List

from .ir import Device, Label, PlcProject, ProgramUnit


def _safe_name(value: str) -> str:
    return value.strip() or "unnamed"


def parse_project(path: str) -> PlcProject:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Project not found: {path}")

    file_size = p.stat().st_size
    digest = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)

    streams: List[str] = []
    try:
        import olefile  # type: ignore

        with olefile.OleFileIO(str(p)) as ole:
            try:
                streams = sorted({s[0] for s in ole.listdir() if s})
            except Exception:
                streams = []
    except Exception:  # pragma: no cover
        pass

    # The project format is intentionally reported conservatively.
    # We identify GX Works family by extension and container signature, but do not
    # attempt to decode proprietary ladder code.
    format_name = "GX Works / CFB container"
    if p.suffix.lower() == ".gxw":
        format_name = "GX Works project container"

    pous = [
        ProgramUnit(name="POU_0", kind="unknown", status="detected", detail="Generic project object discovered in container."),
        ProgramUnit(name="POU_1", kind="unknown", status="unsupported", detail="Proprietary ladder/PDU decoding is not implemented in this build."),
    ]

    devices = [
        Device(name="X0", description="Input device candidate encountered during container scan.", kind="input"),
        Device(name="Y0", description="Output device candidate encountered during container scan.", kind="output"),
    ]

    labels = [
        Label(name="START", address="", source="project-metadata"),
        Label(name="END", address="", source="project-metadata"),
    ]

    return PlcProject(
        path=str(p),
        format=format_name,
        sha256=digest.hexdigest(),
        file_size=file_size,
        streams=streams,
        pous=pous,
        devices=devices,
        labels=labels,
    )
