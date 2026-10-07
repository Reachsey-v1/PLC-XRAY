from __future__ import annotations

import hashlib
import os
from typing import Iterable, List

try:
    import olefile  # type: ignore
except Exception:  # pragma: no cover
    olefile = None


class CfbReader:
    """Minimal Compound File Binary reader wrapper.

    This implementation intentionally keeps the scope narrow and defensively reports
    unsupported structures instead of guessing proprietary ladder logic bytes.
    """

    @staticmethod
    def list_streams(path: str) -> List[str]:
        if olefile is None:
            return []
        try:
            with olefile.OleFileIO(path) as ole:
                return sorted(ole.listdir())
        except Exception:
            return []

    @staticmethod
    def read_metadata(path: str):
        size = os.path.getsize(path)
        digest = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                digest.update(chunk)
        return {
            "file_size": size,
            "sha256": digest.hexdigest(),
        }


__all__ = ["CfbReader"]
