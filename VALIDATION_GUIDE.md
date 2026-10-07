# Production Validation Guide

This guide covers smoke testing and validation procedures for PLC-XRAY v1.2.0 before production deployment.

## Environment Setup

```bash
# Install the package
python -m pip install -e .

# Verify installation
python -m plcxray.cli --help
```

## Test 1: CLI Inspect on Real GXW File

**Objective:** Verify that the CLI can inspect a real Mitsubishi GX Works project without errors.

```bash
# Run inspect on a real project
python -m plcxray.cli inspect path/to/real_project.gxw

# Expected output:
# - Project name and format
# - SHA-256 hash
# - File size in bytes
# - Stream count
# - POU/device/label counts
# - Findings list
# - Verification status
```

**Validation:**
- [ ] Command exits cleanly (return code 0)
- [ ] Output includes all expected fields
- [ ] No errors or stack traces
- [ ] Verification status shows "NOT VERIFIED"

## Test 2: JSON Export

**Objective:** Verify JSON export is valid and contains expected structure.

```bash
# Export to JSON
python -m plcxray.cli inspect path/to/real_project.gxw --json > report.json

# Validate JSON syntax
python -m json.tool < report.json > /dev/null && echo "Valid JSON"

# Inspect structure
python -c "import json; data=json.load(open('report.json')); print(list(data.keys()))"
```

**Expected fields in JSON:**
- `project_name`
- `format`
- `sha256`
- `file_size`
- `streams`
- `pous`
- `devices`
- `labels`
- `metadata`
- `evidence`
- `warnings`

**Validation:**
- [ ] JSON is valid (no parse errors)
- [ ] All expected top-level fields present
- [ ] Evidence records have `source`, `item`, `detail`, `confidence`
- [ ] Warnings list is non-empty

## Test 3: Markdown Report Generation

**Objective:** Verify Markdown report is readable and complete.

```bash
# Generate Markdown report
python -m plcxray.cli report path/to/real_project.gxw --markdown -o report.md

# Check file was created
ls -lh report.md

# View in text editor or markdown viewer
cat report.md
```

**Expected sections:**
- `# PLC-XRAY Inspection Report`
- `## Summary` (with file metadata)
- `## Findings` (with status icons)
- `## Metadata` (extracted fields)
- `## Evidence` (confidence-scored records)
- `## Warnings` (safety disclaimers)

**Validation:**
- [ ] File is created successfully
- [ ] Markdown is properly formatted
- [ ] All sections are present
- [ ] Links and formatting are correct
- [ ] Warnings include "NOT VERIFIED"

## Test 4: GUI Launch and Basic Operations

**Objective:** Verify GUI launches and basic workflow functions.

```bash
# Launch GUI
python PLC-XRAY-GUI.pyw
```

**Manual test steps:**
1. [ ] Window launches with title "PLC-XRAY Professional v1.2.0"
2. [ ] Left panel shows "ENGINEERING" menu items
3. [ ] Status bar shows "READ-ONLY" disclaimer
4. [ ] Click "Open Project" and select real project.gxw
5. [ ] [ ] Header updates with project filename
6. [ ] [ ] Summary panel populates with:
   - Format
   - SHA-256
   - File size
   - Stream/POU/Label/Device counts
   - Verification status
7. [ ] [ ] Findings table displays analysis results
8. [ ] [ ] Status bar updates to "Imported successfully"
9. [ ] [ ] Click "Export JSON"
10. [ ] [ ] Save dialog appears and JSON file is created
11. [ ] [ ] Verify JSON is valid (check with `python -m json.tool`)
12. [ ] [ ] Click "Export Markdown"
13. [ ] [ ] Save dialog appears and Markdown file is created
14. [ ] [ ] Verify Markdown renders correctly

## Test 5: Error Handling

**Objective:** Verify graceful handling of invalid inputs.

```bash
# Try with non-existent file
python -m plcxray.cli inspect nonexistent.gxw 2>&1

# Try with invalid file
echo "invalid data" > fake.gxw
python -m plcxray.cli inspect fake.gxw

# Try with empty file
touch empty.gxw
python -m plcxray.cli inspect empty.gxw
```

**Expected behavior:**
- [ ] Non-existent file: Clear error "Project not found"
- [ ] Invalid file: Graceful handling (may be classified as "GX Works / CFB container")
- [ ] Empty file: Accepted but reports as 0 bytes with no streams
- [ ] No stack traces in any case

## Test 6: Real GXW Sample Data

If you have a real Mitsubishi GX Works project file (e.g., from production), validate:

```bash
# Detailed inspection
python -m plcxray.cli inspect real_project.gxw

# Check for:
# - [ ] Correct file size
# - [ ] Correct SHA-256 (verify manually if possible)
# - [ ] Reasonable stream count (typically 5-50 for real projects)
# - [ ] Non-empty device/label recovery
# - [ ] Meaningful findings
# - [ ] No false positives in evidence
```

## Test 7: Compile and Package Check

```bash
# Verify Python syntax
python -m compileall -q src PLC-XRAY-GUI.pyw

# Run test suite
python -m pytest -v

# Check package structure
python -c "import plcxray; print(plcxray.__version__); print(dir(plcxray))"
```

**Expected:**
- [ ] No compile errors
- [ ] All tests pass
- [ ] Version is "1.2.0"
- [ ] Public API exports are available

## Sign-Off

If all tests pass:
- [ ] Inspection functionality is stable
- [ ] Report generation is reliable
- [ ] GUI workflow is functional
- [ ] Error handling is robust
- [ ] Package structure is correct

**Ready for production use.**

---

**Safety Reminder:** Always verify safety-critical logic using native GX Works tools before deploying to production hardware.
