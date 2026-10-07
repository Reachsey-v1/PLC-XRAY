from __future__ import annotations

from typing import List

from .ir import Finding, PlcProject


def analyze(project: PlcProject) -> List[Finding]:
    findings: List[Finding] = [
        Finding(
            status="INFO",
            title="Container summary",
            detail=f"Project type: {project.format}; file size: {project.file_size:,} bytes; SHA-256: {project.sha256}.",
        ),
        Finding(
            status="INFO",
            title="Stream inventory",
            detail=f"Observed {len(project.streams)} container stream entries.",
        ),
        Finding(
            status="WARNING",
            title="Unsupported logic decode",
            detail="The binary ladder/PDU payload is proprietary and intentionally not reverse-engineered in this implementation.",
        ),
    ]

    if project.devices:
        findings.append(
            Finding(
                status="INFO",
                title="Detected device candidates",
                detail=f"{len(project.devices)} device-like identifiers were recovered from the project container.",
            )
        )
    else:
        findings.append(Finding(status="INFO", title="Detected device candidates", detail="No device names were resolved."))

    if project.labels:
        findings.append(
            Finding(
                status="INFO",
                title="Recovered labels",
                detail=f"{len(project.labels)} label-like names were recovered during container scanning.",
            )
        )
    else:
        findings.append(Finding(status="INFO", title="Recovered labels", detail="No labels were recovered."))

    findings.append(
        Finding(
            status="INFO",
            title="Verification status",
            detail="This tool is read-only and does not claim native GX Works compile/open validation.",
        )
    )
    return findings
