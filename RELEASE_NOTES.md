# Release Notes: PLC-XRAY v1.2.0

**Professional Engineering Inspection Toolkit for Mitsubishi GX Works2/GX Works3**

## Summary

PLC-XRAY v1.2.0 introduces a professional-grade architecture for conservative, evidence-based project inspection. This release refactors the codebase for separation of concerns, adds structured metadata extraction, and provides exportable reports in JSON and Markdown formats.

## What's New

### Evidence-Aware Project Model
Projects are now represented with structured evidence records that capture confidence levels alongside inspection findings. Each scan result is tagged with source (filesystem, container, scanner) and confidence (high, medium, low).

### JSON & Markdown Reports
Generate professional reports with:
- Project summary and metadata
- Container stream inventory
- Detected devices and labels
- Analysis findings with evidence
- Safety disclaimers and verification status

### Enhanced CLI
New command structure:
```bash
python -m plcxray.cli inspect project.gxw [--json]
python -m plcxray.cli report project.gxw [--markdown] [-o output.md]
```

### Professional GUI
The GUI now supports:
- JSON export with full project metadata
- Markdown report export
- Structured summary panel
- Evidence-backed finding display

### Architecture Improvements
- **Parser**: Conservative, read-only GX Works container inspection
- **Analyzer**: Deterministic analysis engine with findings collection
- **Report**: JSON/Markdown templating and export
- **IR**: Rich intermediate representation with evidence tracking

## Safety Boundaries

✅ **Supported:**
- Read-only project inspection
- Conservative metadata/device/label extraction
- JSON and Markdown export
- Evidence-based findings

❌ **Not Supported:**
- Native GX Works compile/open/online verification
- Proprietary ladder/PDU logic decoding
- PLC download or online write operations
- Complete reverse engineering of closed formats

## Installation

```bash
pip install -e .
```

Or use the Windows EXE (if available) from the release assets.

## Quick Start

```bash
# Inspect a project
python -m plcxray.cli inspect project.gxw

# Export Markdown report
python -m plcxray.cli report project.gxw --markdown -o report.md

# Launch GUI
python PLC-XRAY-GUI.pyw
```

## Testing

All changes are covered by tests:
```bash
python -m pytest -v
```

## Known Limitations

- Proprietary ladder logic remains undecoded (intentional)
- Device/label extraction is heuristic-based and conservative
- Native GX Works verification is not performed

## Roadmap

Future releases will explore:
- Full proprietary ladder/PDU decoding
- Device cross-reference semantics
- Timer/counter analysis
- Trace engine and simulation
- GX Works3 native adapter

## Contributors

- **Reachsey-v1**: Architecture and implementation

## License

See LICENSE file in the repository.

---

**Disclaimer:** PLC-XRAY is an inspection-only tool. All safety-critical logic must be verified using native Mitsubishi GX Works tools before deployment to production PLC hardware.
