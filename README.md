# PLC-XRAY v1.2.0

Professional, read-only engineering inspection toolkit for Mitsubishi GX Works2/GX Works3 project analysis.

## Safety boundary
- Original project is never modified by the importer.
- No PLC download, forcing, online write, or physical-machine control is implemented.
- Native GX Works compile/open/online verification is **not** performed by PLC-XRAY.
- Unsupported proprietary structures are reported as NOT VERIFIED / UNSUPPORTED instead of guessed.

## Quick start
```powershell
python -m pip install -e .
python -m plcxray.cli inspect path\to\project.gxw
python -m plcxray.cli report path\to\project.gxw
python PLC-XRAY-GUI.pyw
```

## Source layout
- `src/plcxray/` parser, CFB reader, IR, analyzer, CLI
- `tests/` automated tests
- `assets/` branding/assets notes
- `.github/workflows/` CI and Windows build
- `docs/` architecture and verification notes
