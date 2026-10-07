from plcxray.parser import parse_project


def test_parse_project_smoke(tmp_path):
    project_path = tmp_path / "sample.gxw"
    project_path.write_bytes(b"PLC-XRAY-FAKE-GXW")
    project = parse_project(str(project_path))
    assert project.path == str(project_path)
    assert project.file_size == len(b"PLC-XRAY-FAKE-GXW")
    assert project.format
    assert project.warnings
