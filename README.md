# PLC X-RAY — Professional Engineering Forensic Suite

Evidence-first, read-only analysis software for Mitsubishi GX Works2/GX Works3 project files.

## What it does

- Read-only `.gxw` / CFB inspection
- Nested `_hdb` project database discovery
- POU framing and token inventory
- Global/local declaration indexing
- Device cross-reference
- Writer audit and duplicate-writer findings
- Instruction/advanced-instruction lexical audit
- Trace / WHY for decoded device evidence
- Global search
- Deterministic health score and verification gate
- PLC-IR JSON export and engineering HTML reports
- Project diff and CLI verification commands
- Professional Windows GUI

## Evidence states

Every important conclusion is constrained to `CONFIRMED`, `INFERRED`, `NOT VERIFIED`, `UNKNOWN`, or `UNSUPPORTED`. The software never claims GX Works native compile, online monitoring, PLC download, force, or physical-machine validation unless those actions are actually performed outside PLC X-RAY.

## Safety boundary

PLC X-RAY is read-only. It does not modify the original GXW, download to a PLC, force outputs, or bypass safety interlocks.

## Windows build

On Windows, run `BUILD_WINDOWS_EXE.bat`. The script runs tests before PyInstaller. GitHub Actions performs the same test/build flow and publishes `PLC-XRAY.exe` as a workflow artifact; version tags create releases.

## CLI

```text
plcxray inspect project.gxw
plcxray parse project.gxw --json
plcxray devices project.gxw --type M
plcxray trace project.gxw M3004 --json
plcxray why project.gxw M3004
plcxray health project.gxw --json
plcxray verify project.gxw --json
plcxray diff old.gxw new.gxw --json
plcxray report project.gxw
```

## Verification boundary

Static analysis can be completed locally. Native GX Works2/3 open/compile, online monitoring, download, and physical machine testing remain explicit engineering verification gates.
