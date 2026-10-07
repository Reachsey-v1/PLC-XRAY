# GitHub Release Text for v1.2.0

Copy and paste this text into the GitHub Release description field.

---

## PLC-XRAY v1.2.0: Professional Engineering Inspection Toolkit

**Read-only GX Works2/GX Works3 project analysis with evidence-based findings and exportable reports.**

### 🎯 Overview

This release introduces a professional-grade architecture for conservative, deterministic inspection of Mitsubishi GX Works projects. The codebase has been refactored for separation of concerns, structured metadata extraction, and exportable reports in JSON and Markdown formats.

### ✨ Major Features

#### Evidence-Aware Project Model
- Structured capture of inspection evidence with confidence levels
- Evidence tagged with source (filesystem, container, scanner) and confidence (high, medium, low)
- Rich project metadata including device/label candidates
- Safety disclaimers and verification status

#### Report Generation
- **JSON export**: Complete project serialization with metadata and evidence
- **Markdown export**: Human-readable reports with findings, metadata, evidence, and warnings
- Structured summary panels with key metrics

#### Enhanced CLI
Two main commands:
```bash
# Inspect a project
python -m plcxray.cli inspect project.gxw [--json]

# Generate reports
python -m plcxray.cli report project.gxw [--markdown] [-o output.md]
```

#### Professional GUI
- Dark-mode project browser
- Real-time summary and findings display
- JSON export with full metadata
- Markdown report export
- Evidence-backed findings table

#### Architecture Improvements
- **Parser**: Conservative, read-only GX Works container inspection
- **Analyzer**: Deterministic analysis engine with findings collection
- **Report**: Templated JSON and Markdown generation
- **IR**: Rich intermediate representation with evidence tracking
- **Engines**: Abstracted analysis pipeline for extensibility

### 🔒 Safety Boundaries (Unchanged)

**Supported:**
- ✅ Read-only project inspection
- ✅ Conservative metadata/device/label extraction
- ✅ JSON and Markdown export
- ✅ Evidence-based findings with confidence scoring

**Not Supported:**
- ❌ Native GX Works compile/open/online verification
- ❌ Proprietary ladder/PDU logic decoding
- ❌ PLC download or online write operations
- ❌ Complete reverse engineering of closed formats

### 📦 Installation

```bash
# From source
pip install -e .

# From GitHub release
pip install git+https://github.com/Reachsey-v1/PLC-XRAY.git@v1.2.0
```

### 🚀 Quick Start

```bash
# Inspect a project
python -m plcxray.cli inspect project.gxw

# Export JSON report
python -m plcxray.cli inspect project.gxw --json > report.json

# Export Markdown report
python -m plcxray.cli report project.gxw --markdown -o report.md

# Launch GUI
python PLC-XRAY-GUI.pyw
```

### 📋 What's Changed

#### Added
- Evidence-aware project model with confidence levels
- Rich metadata extraction (filename, extension, size, hash, type)
- Report generation engine (JSON and Markdown)
- Enhanced CLI with structured subcommands
- GUI export support (JSON and Markdown)
- Professional analysis engine abstraction
- Comprehensive test suite (parser, IR, CLI, report)
- Package public API exports
- Safety documentation and release materials

#### Changed
- Architecture: Separated parser, analyzer, and report generation
- IR model: Enhanced with evidence, metadata, warnings
- CLI: Improved help text and command structure
- GUI: Direct binding to project model with export buttons

#### Fixed
- Improved device/label extraction robustness
- Better error handling in container parsing
- Clearer unsupported-feature warnings

### 🧪 Testing

All changes are covered by automated tests:

```bash
python -m pytest -v
```

**Test coverage:**
- Parser: GXW file parsing, metadata extraction, device/label recovery
- IR: Project model serialization, evidence tracking
- CLI: Command parsing, JSON/Markdown output
- Report: JSON and Markdown generation

### 📚 Documentation

- **README.md**: Installation, quick start, architecture overview
- **CHANGELOG.md**: Detailed change history
- **RELEASE_NOTES.md**: Release summary and features
- **VALIDATION_GUIDE.md**: Smoke testing procedures with real GXW files
- **RELEASE_CHECKLIST.md**: Pre-release validation checklist
- **RELEASE_COMMANDS.md**: Step-by-step release execution

### 🗺️ Roadmap

Future releases planned to explore:
- [ ] Full proprietary ladder/PDU decoding (major release)
- [ ] Device cross-reference semantics
- [ ] Timer/counter semantic analyzer
- [ ] WHY/backward/forward trace engine
- [ ] Simulation and regression test engine
- [ ] GX Works3 native adapter improvements
- [ ] Native GX Works verification adapter

### 🔗 Links

- **Repository**: https://github.com/Reachsey-v1/PLC-XRAY
- **Issues**: https://github.com/Reachsey-v1/PLC-XRAY/issues
- **Documentation**: See repository README.md

### ⚠️ Important Notes

**Safety Disclaimer:**
PLC-XRAY is a read-only inspection tool only. All safety-critical logic **must** be verified using native Mitsubishi GX Works tools (compile, open, online test) before deployment to production PLC hardware.

**Verification Status:**
- Container inspection: ✅ Supported
- Metadata extraction: ✅ Supported
- Report generation: ✅ Supported
- Native GX Works verification: ❌ Not performed
- Proprietary logic decode: ❌ Not attempted
- PLC online operations: ❌ Not supported

### 👤 Contributors

- **Reachsey-v1**: Architecture, implementation, and testing

### 📄 License

See LICENSE file in the repository.

---

**Thank you for using PLC-XRAY!**

