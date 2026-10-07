from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Evidence:
    source: str
    item: str
    detail: str
    confidence: str = "low"


@dataclass
class Finding:
    status: str
    title: str
    detail: str


@dataclass
class ProgramUnit:
    name: str
    kind: str = "unknown"
    status: str = "unknown"
    detail: str = ""


@dataclass
class Device:
    name: str
    description: str = ""
    kind: str = "device"


@dataclass
class Label:
    name: str
    address: str = ""
    source: str = "unknown"


@dataclass
class PlcProject:
    path: str
    format: str
    sha256: str
    file_size: int
    streams: List[str] = field(default_factory=list)
    pous: List[ProgramUnit] = field(default_factory=list)
    devices: List[Device] = field(default_factory=list)
    labels: List[Label] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    project_name: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    evidence: List[Evidence] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "project_name": self.project_name,
            "format": self.format,
            "sha256": self.sha256,
            "file_size": self.file_size,
            "metadata": self.metadata,
            "streams": self.streams,
            "pous": [
                {
                    "name": p.name,
                    "kind": p.kind,
                    "status": p.status,
                    "detail": p.detail,
                }
                for p in self.pous
            ],
            "devices": [
                {"name": d.name, "description": d.description, "kind": d.kind}
                for d in self.devices
            ],
            "labels": [
                {"name": l.name, "address": l.address, "source": l.source}
                for l in self.labels
            ],
            "warnings": self.warnings,
            "evidence": [
                {
                    "source": e.source,
                    "item": e.item,
                    "detail": e.detail,
                    "confidence": e.confidence,
                }
                for e in self.evidence
            ],
        }


__all__ = ["Evidence", "Finding", "ProgramUnit", "Device", "Label", "PlcProject"]
