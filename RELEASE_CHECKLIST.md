# Release Checklist for v1.2.0

Use this checklist to validate the release before tagging.

## Pre-Release Validation

- [ ] All tests pass: `python -m pytest -v`
- [ ] Compile check passes: `python -m compileall -q src PLC-XRAY-GUI.pyw`
- [ ] README is up-to-date
- [ ] CHANGELOG.md reflects all changes
- [ ] version in `src/plcxray/__init__.py` is correct (`__version__ = "1.2.0"`)
- [ ] version in `pyproject.toml` is correct (`version = "1.2.0"`)
- [ ] No uncommitted changes: `git status` shows clean working tree

## Smoke Test (with real GXW file)

```bash
# CLI inspect
python -m plcxray.cli inspect path/to/real/project.gxw

# CLI JSON export
python -m plcxray.cli inspect path/to/real/project.gxw --json > report.json
cat report.json  # Verify valid JSON

# CLI Markdown report
python -m plcxray.cli report path/to/real/project.gxw --markdown -o report.md
cat report.md  # Verify readable markdown

# GUI test (manual)
python PLC-XRAY-GUI.pyw
# - Open project.gxw
# - Verify summary displays correctly
# - Export JSON and verify it's valid
# - Export Markdown and verify it's readable
```

## Release Steps

1. **Ensure branch is clean**
   ```bash
   git status
   git log --oneline -5
   ```

2. **Merge to main**
   ```bash
   git checkout main
   git merge feat/professional-upgrade
   ```

3. **Create Git tag**
   ```bash
   git tag -a v1.2.0 -m "Release v1.2.0: Professional upgrade with evidence-aware inspection, JSON/Markdown reports, and enhanced GUI"
   git push origin main --tags
   ```

4. **Create GitHub Release**
   - Go to [GitHub Releases](https://github.com/Reachsey-v1/PLC-XRAY/releases)
   - Click "Draft a new release"
   - Select tag: `v1.2.0`
   - Title: `PLC-XRAY v1.2.0: Professional Engineering Inspection Toolkit`
   - Use RELEASE_NOTES.md as description
   - Attach Windows EXE from GitHub Actions if available
   - Publish release

## Post-Release

- [ ] Verify release is live on GitHub
- [ ] Test installation: `pip install git+https://github.com/Reachsey-v1/PLC-XRAY.git@v1.2.0`
- [ ] Update project documentation if needed
- [ ] Announce release in relevant channels

---

**Release Manager Notes:**
- This is a significant architectural upgrade from v1.1.0
- Safety boundaries remain unchanged (read-only, no native verification)
- All tests must pass before release
- Real-sample smoke test strongly recommended
