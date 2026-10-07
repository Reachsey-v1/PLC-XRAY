# Test Status — PLC X-RAY 1.2.0

## Automated validation

- Python compile: PASS
- Pytest: **12 passed**
- Real GXW parser regression: PASS against `/mnt/data/APEX_JPZ2QI_PLCN2114_25080615(2).gxw`
- Input SHA-256 preservation: PASS (`80e8fda561e2764befa9371bd4591aeeecced9a011099607dda098984a01cc1e`)
- GUI smoke test under Xvfb with real GXW: PASS
- Trace/WHY smoke test: PASS (`M3004`)
- HTML report generation with real GXW: PASS
- CLI inspect/health/verify/trace: PASS

## Windows verification

- Native Windows EXE build: **NOT EXECUTED in this Linux environment** because PyInstaller is not installed and external package download is unavailable.
- GitHub Actions Windows build: workflow configured, **NOT EXECUTED here**.
- GX Works2/GX Works3 native open/compile: **NOT EXECUTED**.
- Online PLC monitoring/download/force: **NOT EXECUTED**.
- Physical machine test: **NOT EXECUTED**.

## Engineering gate

The supplied APEX project currently has duplicate writer targets and incomplete native verification. Therefore PLC X-RAY reports **NOT READY — STATIC REVIEW REQUIRED** for that project rather than claiming a false READY state.
