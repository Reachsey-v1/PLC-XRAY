# PLC X-RAY Final GUI

A Windows desktop GUI for evidence-first, read-only analysis of Mitsubishi GX Works `.gxw` projects.

## Easiest start
Double-click **`run_gui.bat`**. Then choose **Open GXW…**.

## Build a standalone EXE
On Windows with Python 3 installed, double-click **`BUILD_WINDOWS_EXE.bat`**. It installs PyInstaller if needed and creates:

`dist\PLC-XRAY.exe`

The EXE is a GUI application and does not open a console window.

## GitHub Actions
The included `.github/workflows/build-windows.yml` builds `PLC-XRAY.exe` on a Windows GitHub runner when manually dispatched or when a `v*` tag is pushed.

## Safety
- Source `.gxw` is read-only.
- No PLC download, force, online monitoring or physical control.
- No claim of GX Works2 native compile/open verification.
- Unsupported binary areas are explicitly marked `NOT VERIFIED`.
