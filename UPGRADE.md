# PLC-XRAY Professional Upgrade

This branch contains the professional-grade upgrade for PLC-XRAY v1.2.0, including:

## Features Added

- **Evidence-aware metadata model** — structured capture of project inspection evidence with confidence levels
- **Rich project serialization** — comprehensive JSON export including metadata, evidence, and findings
- **Report generation** — JSON and Markdown report templates for project analysis
- **Enhanced CLI** — `inspect` and `report` commands with JSON/Markdown output modes
- **Professional test suite** — smoke tests for parser, analyzer, CLI, and report generation
- **Package-level exports** — clean public API for downstream tooling

## Architecture

```
src/plcxray/
├── __init__.py          # Package exports
├── ir.py               # Intermediate representation (Evidence, Finding, PlcProject, etc.)
├── parser.py           # GX Works container parser (conservative, read-only)
├── analyzer.py         # Project analysis and findings generation
├── report.py           # Report generation (JSON and Markdown)
└── cli.py              # Command-line interface

tests/
├── test_ir.py          # IR model tests
├── test_cfb.py         # Parser tests
├── test_cli.py         # CLI command tests
└── test_report.py      # Report generation tests
```

## Safety Boundaries

- ✅ Read-only container inspection
- ✅ Conservative device/label extraction
- ✅ Explicit unsupported ladder/PDU decode warnings
- ❌ No proprietary logic reverse-engineering
- ❌ No native GX Works verification claims
- ❌ No PLC download, online write, or device control

## Usage Examples

### Inspect a project
```bash
python -m plcxray.cli inspect project.gxw
python -m plcxray.cli inspect project.gxw --json
```

### Generate reports
```bash
python -m plcxray.cli report project.gxw --markdown -o report.md
python -m plcxray.cli report project.gxw --json -o report.json
```

## Testing

```bash
python -m pytest -v tests/
```

## Next Steps (Future Roadmap)

- [ ] Full proprietary ladder/PDU decoding (roadmap item)
- [ ] Complete device cross-reference semantics
- [ ] Timer/counter semantic analyzer
- [ ] Trace engine (WHY/backward/forward)
- [ ] Simulation and regression test engine
- [ ] GX Works3 adapter improvements
- [ ] Native GX Works verification adapter
