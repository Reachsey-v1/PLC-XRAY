# Release Command Sequence for v1.2.0

Execute these commands in order to release PLC-XRAY v1.2.0.

## Step 1: Verify Branch Status

```bash
# Check current branch
git branch --show-current
# Expected output: feat/professional-upgrade

# Verify clean working tree
git status
# Expected: nothing to commit, working tree clean

# Show recent commits
git log --oneline -10
```

## Step 2: Run Pre-Release Tests

```bash
# Install dependencies
python -m pip install -e .

# Run full test suite
python -m pytest -v
# Expected: All tests pass

# Verify Python compilation
python -m compileall -q src PLC-XRAY-GUI.pyw
# Expected: No output (success)

# Verify package imports
python -c "from plcxray import __version__; print(f'PLC-XRAY v{__version__}')"
# Expected: PLC-XRAY v1.2.0
```

## Step 3: Smoke Test (Optional but Recommended)

If you have a real GXW file available:

```bash
# Test CLI inspect
python -m plcxray.cli inspect /path/to/real_project.gxw

# Test JSON export
python -m plcxray.cli inspect /path/to/real_project.gxw --json | python -m json.tool > /dev/null && echo "JSON Valid"

# Test Markdown report
python -m plcxray.cli report /path/to/real_project.gxw --markdown -o /tmp/test_report.md
head -20 /tmp/test_report.md
```

## Step 4: Merge to Main Branch

```bash
# Switch to main
git checkout main

# Verify main is up to date (if working with upstream)
git pull origin main
# (May skip if working locally only)

# Merge feature branch
git merge --no-ff feat/professional-upgrade -m "Merge feat/professional-upgrade: v1.2.0 professional upgrade"

# Verify merge
git log --oneline -5
# Should show merge commit at top
```

## Step 5: Create Annotated Git Tag

```bash
# Create tag with message
git tag -a v1.2.0 -m "Release v1.2.0: Professional Engineering Inspection Toolkit

Major features:
- Evidence-aware project model with confidence scoring
- JSON and Markdown report generation
- Enhanced CLI with inspect/report commands
- Professional GUI with export support
- Comprehensive test suite
- Safety boundary documentation

Safety boundaries preserved:
- Read-only inspection only
- No native GX Works verification claims
- No proprietary ladder decode guessing
- No PLC online operations

See CHANGELOG.md and RELEASE_NOTES.md for details."

# Verify tag was created
git tag -l

# Show tag details
git show v1.2.0
```

## Step 6: Push to GitHub

```bash
# Push main branch
git push origin main

# Push tag
git push origin v1.2.0

# Verify on GitHub (takes a moment to sync)
git ls-remote origin | grep v1.2.0
```

## Step 7: Create GitHub Release

### Option A: Using GitHub Web UI (Recommended)

1. Visit: https://github.com/Reachsey-v1/PLC-XRAY/releases
2. Click **"Draft a new release"**
3. Select tag: **v1.2.0**
4. Title: **PLC-XRAY v1.2.0: Professional Engineering Inspection Toolkit**
5. Copy the release notes text from `RELEASE_NOTES.md` into the description field
6. **Publish release**

### Option B: Using GitHub CLI (if installed)

```bash
# Requires gh CLI tool installed and authenticated
gh release create v1.2.0 \
  --title "PLC-XRAY v1.2.0: Professional Engineering Inspection Toolkit" \
  --notes-file RELEASE_NOTES.md
```

## Step 8: Verify Release

```bash
# Check GitHub release was created
git ls-remote --tags origin | grep v1.2.0

# Verify release shows on GitHub
# https://github.com/Reachsey-v1/PLC-XRAY/releases/tag/v1.2.0

# Test installation from GitHub tag
pip install git+https://github.com/Reachsey-v1/PLC-XRAY.git@v1.2.0

# Verify installed version
python -c "import plcxray; print(f'Installed: {plcxray.__version__}')"
```

## Step 9: Post-Release

```bash
# Update local branch tracking
git fetch origin

# Switch to develop/next feature branch if desired
git checkout -b feat/next-feature

# Document the release completion
echo "v1.2.0 released successfully"
```

## Rollback (if needed)

If something goes wrong before step 8:

```bash
# Delete local tag
git tag -d v1.2.0

# Reset main to previous commit
git reset --hard HEAD~1

# Switch back to feature branch
git checkout feat/professional-upgrade
```

If tag was already pushed to GitHub:

```bash
# Delete remote tag
git push origin --delete v1.2.0

# Delete local tag
git tag -d v1.2.0
```

---

## Summary

**Total steps:** 9 major phases
**Estimated time:** 10-15 minutes (excluding optional smoke test)
**Success criteria:**
- All tests pass
- Tag created and pushed
- GitHub release published
- Installation from tag works

