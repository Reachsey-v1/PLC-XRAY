from __future__ import annotations

from typing import Any, Dict, List

from .ir import Device, Evidence, Finding, Label, PlcProject, ProgramUnit


def _normalize_name(value: str) -> str:
    if not value:
        return "unknown"
    cleaned = value.strip().replace("\\", "/")
    if cleaned.startswith("/"):
        cleaned = cleaned.lstrip("/")
    return cleaned.split("/")[-1] or "unknown"


def build_summary(project: PlcProject) -> Dict[str, Any]:
    return {
        "project_name": project.project_name,
        "format": project.format,
        "sha256": project.sha256,
        "file_size": project.file_size,
        "stream_count": len(project.streams),
        "pou_count": len(project.pous),
        "device_count": len(project.devices),
        "label_count": len(project.labels),
        "warning_count": len(project.warnings),
    }


def collect_findings(project: PlcProject) -> List[Finding]:
    findings: List[Finding] = [
        Finding(
            status="INFO",
            title="Project overview",
            detail=(
                f"Project {project.project_name} classified as {project.format}; "
                f"{project.file_size:,} bytes; SHA-256 {project.sha256}."
            ),
        ),
        Finding(
            status="INFO",
            title="Container streams",
            detail=f"Detected {len(project.streams)} stream entries in the container.",
        ),
        Finding(
            status="WARNING",
            title="Unsupported logic decode",
            detail="Proprietary ladder/PDU semantics are intentionally left unsupported.",
        ),
        Finding(
            status="INFO",
            title="Verification boundary",
            detail="This inspection is read-only and does not claim native GX Works verification.",
        ),
    ]

    if project.devices:
        findings.append(
            Finding(
                status="INFO",
                title="Devices",
                detail=f"Recovered {len(project.devices)} device-like entries from the project scan.",
            )
        )
    if project.labels:
        findings.append(
            Finding(
                status="INFO",
                title="Labels",
                detail=f"Recovered {len(project.labels)} label-like entries from the project scan.",
            )
        )
    if project.metadata:
        findings.append(
            Finding(
                status="INFO",
                title="Metadata",
                detail=f"Container metadata includes {len(project.metadata)} extracted fields.",
            )
        )
    return findings


__all__ = ["build_summary", "collect_findings", "_normalize_name"]
