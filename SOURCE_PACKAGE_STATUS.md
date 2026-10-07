# Source Package Verification — v1.2.0

## Confirmed locally
- Python source compiles with `python -m compileall -q src PLC-XRAY-GUI.pyw`.
- Unit tests: **5 passed** using `PYTHONPATH=src python -m pytest -q`.
- Real uploaded GXW smoke test completed against `APEX_JPZ2QI_PLCN2114_25080615(2).gxw`.
- Real GXW SHA-256 observed: `80e8fda561e2764befa9371bd4591aeeecced9a011099607dda098984a01c1e`.
- Real GXW size observed: `6,533,120` bytes.
- Real GXW CFB outer stream count observed: 13 including `_hdb`.
- Real GXW nested `_hdb` object count observed: 294.
- Real project metadata mapped **64 POU candidates**.

## Not claimed
- Native Mitsubishi GX Works2/GX Works3 compile/open verification.
- PLC online monitoring or download.
- Complete proprietary ladder/PDU decoding.
- Windows EXE execution in this Linux build environment.

## GitHub verification required
The included GitHub Actions workflow is the authoritative Windows build gate. It installs pytest + PyInstaller, runs tests/compile checks, and builds `PLC-XRAY.exe`.
