from __future__ import annotations

import argparse
import json
from pathlib import Path

from .analyzer import analyze
from .parser import parse_project


def _inspect(path: str) -> None:
    project = parse_project(path)
    print(f"Format: {project.format}")
    print(f"SHA-256: {project.sha256}")
    print(f"File size: {project.file_size:,} bytes")
    print(f"Streams: {len(project.streams)}")
    print(f"POUs: {len(project.pous)}")
    print(f"Labels: {len(project.labels)}")
    print(f"Devices: {len(project.devices)}")
    print("Verification: NOT VERIFIED — project is inspected read-only, not compiled or opened by GX Works")
    for finding in analyze(project):
        print(f"[{finding.status}] {finding.title}: {finding.detail}")


def _report(path: str, output: str | None = None) -> None:
    project = parse_project(path)
    payload = project.to_dict()
    if output:
        Path(output).write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"Report written to {output}")
    else:
        print(json.dumps(payload, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="PLC-XRAY read-only GX Works inspection")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Inspect a GX Works project container")
    inspect_parser.add_argument("path")

    report_parser = subparsers.add_parser("report", help="Export a project report as JSON")
    report_parser.add_argument("path")
    report_parser.add_argument("-o", "--output", default=None)

    args = parser.parse_args()

    if args.command == "inspect":
        _inspect(args.path)
    elif args.command == "report":
        _report(args.path, args.output)


if __name__ == "__main__":
    main()
