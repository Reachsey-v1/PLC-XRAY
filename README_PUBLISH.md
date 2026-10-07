# PLC X-RAY — Professional Windows GUI

Professional read-only engineering analysis software for Mitsubishi GX Works2/GX Works3 PLC projects.

## Publish to GitHub

1. Extract this package.
2. Double-click `PUBLISH_TO_GITHUB.bat`.
3. If Git asks for authentication, complete the GitHub login in the Windows credential flow.
4. The script pushes `main` and tag `v1.1.0`.
5. GitHub Actions builds the Windows EXE.
6. Download `PLC-XRAY.exe` from GitHub Releases after the workflow succeeds.

Repository:

https://github.com/Reachsey-v1/PLC-XRAY

## Safety

- PLC X-RAY operates read-only on imported PLC project files.
- It does not download to PLCs, force outputs, or bypass safety circuits.
- Native GX Works2/GX Works3 compile/online verification is not claimed unless separately performed.
- Do not commit private `.gxw` projects to this public repository.

## Release boundary

The Windows EXE is produced by GitHub Actions on a Windows runner. The source package includes automated tests and the build workflow.
