from plcxray.parser import parse_project
import pytest


def test_parse_project_smoke(tmp_path):
    project_path = tmp_path / "sample.gxw"
    project_path.write_bytes(b"PLC-XRAY-FAKE-GXW")
    project = parse_project(str(project_path))
    assert project.path == str(project_path)
    assert project.file_size == len(b"PLC-XRAY-FAKE-GXW")
    assert project.format == "GX Works project container"
    assert project.warnings
    assert project.metadata
    assert project.evidence


def test_parse_project_missing(tmp_path):
    missing_path = tmp_path / "missing.gxw"
    with pytest.raises(FileNotFoundError):
        parse_project(str(missing_path))


def test_parse_project_g3(tmp_path):
    project_path = tmp_path / "sample.g3"
    project_path.write_bytes(b"GX3-DATA")
    project = parse_project(str(project_path))
    assert project.format == "GX Works3 project container"
