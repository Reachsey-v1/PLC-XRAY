from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AnalysisEngineResult:
    project_name: str
    format: str
    sha256: str
    summary: Dict[str, Any] = field(default_factory=dict)
    findings: List[Dict[str, str]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)


__all__ = ["AnalysisEngineResult"]
