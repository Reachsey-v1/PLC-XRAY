# Changelog

All notable changes to PLC-XRAY are documented in this file.

## [1.2.0] - 2026-10-07

### Added
- **Evidence-aware project model**: Structured capture of inspection evidence with confidence levels
- **Rich metadata extraction**: Project name, container type, file hash, stream inventory
- **Report generation**: JSON and Markdown export formats with structured findings
- **Enhanced CLI**: `inspect` and `report` commands with JSON/Markdown output modes
- **GUI export support**: Export JSON and Markdown reports directly from the GUI
- **Professional analysis engine**: Abstracted analysis pipeline with findings collection
- **Comprehensive test suite**: Parser, IR, CLI, and report generation tests
- **Package exports**: Clean public API for downstream tooling
- **Safety documentation**: Explicit boundary documentation between supported and unsupported features

### Changed
- **Architecture**: Separated parser, analyzer, and report generation into distinct modules
- **IR model**: Enhanced PlcProject with evidence, metadata, and warnings fields
- **CLI interface**: Improved help text and command structure
- **GUI workflow**: Bind project model directly to GUI components

### Fixed
- Improved device/label extraction robustness
- Better error handling in container parsing
- Clearer unsupported-feature warnings

### Safety Notes
- Continues to avoid claiming native GX Works verification
- Maintains read-only inspection approach
- Does not attempt proprietary ladder logic reverse engineering

## [1.1.0] - Prior Release

See git history for earlier versions.

---

**Note:** Version numbering follows semantic versioning (MAJOR.MINOR.PATCH).
