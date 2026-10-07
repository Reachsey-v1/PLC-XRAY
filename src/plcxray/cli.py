from __future__ import annotations

import argparse
import json
from pathlib import Path

from .analyzer import analyze
from .parser import parse_project
from .report import report_json, report_markdown


def _emit_project(project, as_json: bool) -> None:
    if as_json:
        print(json.dumps(project.to_dict(), indent=2))
        return

    print(f"Project: {project.project_name}")
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


def _inspect(path: str, as_json: bool = False) -> None:
    project = parse_project(path)
    _emit_project(project, as_json)


def _report(
    path: str, output: str | None = None, as_json: bool = False, as_markdown: bool = False
) -> None:
    project = parse_project(path)

    if as_markdown:
        content = report_markdown(project)
        if output:
            Path(output).write_text(content, encoding="utf-8")
            print(f"Markdown report written to {output}")
        else:
            print(content)
    else:
        payload = project.to_dict()
        if output:
            Path(output).write_text(json.dumps(payload, indent=2), encoding="utf-8")
            print(f"JSON report written to {output}")
        elif as_json:
            print(json.dumps(payload, indent=2))
        else:
            _emit_project(project, False)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PLC-XRAY v1.2.0 — Read-only GX Works project inspection toolkit",
        epilog="All operations are read-only. Native GX Works verification is not performed.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Inspect a GX Works project container")
    inspect_parser.add_argument("path", help="Path to .gxw or .g3 project file")
    inspect_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON output")

    report_parser = subparsers.add_parser(
        "report", help="Generate a structured report for a GX Works project"
    )
    report_parser.add_argument("path", help="Path to .gxw or .g3 project file")
    report_parser.add_argument(
        "-o", "--output", default=None, help="Output file path (JSON or Markdown)"
    )
    report_parser.add_argument(
        "--json", action="store_true", help="Emit JSON report to stdout"
    )
    report_parser.add_argument(
        "--markdown",
        action="store_true",
        help="Generate Markdown report (use with -o or default to stdout)",
    )

    args = parser.parse_args()

    if args.command == "inspect":
        _inspect(args.path, args.json)
    elif args.command == "report":
        _report(args.path, args.output, args.json, args.markdown)


if __name__ == "__main__":
    main()
