from __future__ import annotations

import hashlib
import os
from typing import List

try:
    import olefile  # type: ignore
except Exception:  # pragma: no cover
    olefile = None


class CfbReader:
    """Minimal GX Works / CFB container reader.

    This implementation intentionally stops at the container boundary and does not
    try to interpret proprietary ladder/PDU binary payloads.
    """

    @staticmethod
    def list_streams(path: str) -> List[str]:
        if olefile is None:
            return []
        try:
            with olefile.OleFileIO(path) as ole:
                names: List[str] = []
                for entry in ole.listdir():
                    if entry:
                        names.append("/".join(str(part) for part in entry))
                return sorted(set(names))
        except Exception:
            return []

    @staticmethod
    def read_metadata(path: str):
        size = os.path.getsize(path)
        digest = hashlib.sha256()
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return {"file_size": size, "sha256": digest.hexdigest()}


__all__ = ["CfbReader"]
