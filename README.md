# PLC-XRAY v1.2.0

**Professional read-only engineering inspection toolkit for Mitsubishi GX Works2/GX Works3 PLC project analysis.**

PLC-XRAY provides conservative, evidence-based project inspection without attempting proprietary logic decode or claiming native GX Works verification.

## Features

- 📋 **Project metadata extraction**: SHA-256, file size, stream count, device/label recovery
- 🔍 **Read-only container inspection**: Conservative CFB parser with no data modification
- 📊 **Report generation**: JSON and Markdown exports with structured evidence
- 🖥️ **Professional GUI**: Dark-mode project browser with export options
- 💻 **CLI tools**: `inspect` and `report` commands for automation
- ✅ **Comprehensive tests**: Parser, IR, CLI, and report generation validation

## Safety Boundaries

✅ **Safe:**
- Read-only project inspection
- Conservative metadata extraction
- Evidence-based findings
- Explicit unsupported-logic warnings

❌ **Not Supported:**
- Native GX Works verification (compile/open/online)
- Proprietary ladder/PDU logic decoding
- PLC download, online write, or device control
- Complete reverse engineering of closed formats

## Quick Start

### Installation
```bash
python -m pip install -e .
```

### CLI Usage

**Inspect a project:**
```bash
python -m plcxray.cli inspect project.gxw
python -m plcxray.cli inspect project.gxw --json
```

**Generate reports:**
```bash
python -m plcxray.cli report project.gxw --markdown -o report.md
python -m plcxray.cli report project.gxw --json -o report.json
```

### GUI
```bash
python PLC-XRAY-GUI.pyw
```

1. Click **Open Project** and select a `.gxw` or `.g3` file
2. Review the summary panel (SHA-256, streams, POUs, devices, labels)
3. Examine analysis findings in the table
4. Export JSON or Markdown report for documentation

## Architecture

```
src/plcxray/
├── __init__.py          # Package exports
├── ir.py               # Intermediate representation (PlcProject, Evidence, Finding, etc.)
├── parser.py           # GX Works container parser
├── analyzer.py         # Project analysis and findings
├── report.py           # JSON and Markdown report generation
├── engines.py          # Analysis engine abstractions
├── cfb.py              # Compound File Binary utilities
└── cli.py              # Command-line interface

tests/
├── test_ir.py
├── test_cfb.py
├── test_cli.py
└── test_report.py
```

## Report Format

Generated reports include:
- **Summary**: File metadata, stream count, POUs, devices, labels
- **Findings**: Container type, evidence captured, device candidates, verification status
- **Metadata**: Extracted project properties
- **Evidence**: Confidence-scored scan results
- **Warnings**: Safety and verification disclaimers

## Testing

```bash
# Run tests
python -m pytest -v

# Compile check
python -m compileall -q src PLC-XRAY-GUI.pyw
```

## Verification Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Read-only inspection | ✅ Supported | Container is never modified |
| Metadata extraction | ✅ Supported | SHA-256, streams, device/label recovery |
| Report generation | ✅ Supported | JSON and Markdown formats |
| Native GX Works verification | ❌ Not performed | Use native GX Works for compilation/online testing |
| Proprietary logic decode | ❌ Not attempted | Intentionally excluded to avoid guessing |
| PLC online operations | ❌ Not supported | No download, write, or device control |

## Roadmap

- [ ] Full proprietary ladder/PDU decoding (future major release)
- [ ] Device cross-reference semantics
- [ ] Timer/counter semantic analyzer
- [ ] WHY/backward/forward trace engine
- [ ] Simulation and regression test engine
- [ ] GX Works3 adapter improvements
- [ ] Native GX Works verification adapter

## License

See LICENSE file for details.

## Support

For issues, feature requests, or documentation improvements, visit the [GitHub repository](https://github.com/Reachsey-v1/PLC-XRAY).

---

**Disclaimer:** PLC-XRAY is an inspection-only tool. All safety-critical logic must be verified using native Mitsubishi GX Works tools before deployment to production PLC hardware.
