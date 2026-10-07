# Test Status

Local source-package gate: **PENDING EXECUTION** at package creation time.

Required GitHub gate:
1. Install package.
2. Run `python -m pytest -q`.
3. Run compile check with `python -m compileall -q src PLC-XRAY-GUI.pyw`.
4. Build Windows executable with PyInstaller.
5. Upload artifact.
6. Manually test the EXE with a real GXW.
7. Native GX Works verification remains external and is never claimed by this project.
