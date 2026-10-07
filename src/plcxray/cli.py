from __future__ import annotations

from typing import List

from .ir import Finding, PlcProject


def analyze(project: PlcProject) -> List[Finding]:
    findings: List[Finding] = []
    findings.append(
        Finding(
            status="INFO",
            title="Container type",
            detail=f"Project identified as {project.format}.",
        )
    )
    findings.append(
        Finding(
            status="INFO",
            title="File summary",
            detail=f"SHA-256 {project.sha256}; {project.file_size:,} bytes; {len(project.streams)} streams; {len(project.pous)} POU entries.",
        )
    )
    findings.append(
        Finding(
            status="WARNING",
            title="Unsupported ladder logic decode",
            detail="Proprietary ladder/PDU opcodes are intentionally not guessed. The project is read-only and the logic remains unverified.",
        )
    )
    if not project.devices:
        findings.append(Finding("INFO", "Devices", "No device references were extracted."))
    else:
        findings.append(
            Finding(
                "INFO",
                "Devices",
                f"{len(project.devices)} device candidates discovered in project metadata.",
            )
        )
    if not project.labels:
        findings.append(Finding("INFO", "Labels", "No labels were extracted."))
    else:
        findings.append(
            Finding(
                "INFO",
                "Labels",
                f"{len(project.labels)} label entries extracted from the project container.",
            )
        )
    return findings
