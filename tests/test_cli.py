from plcxray.ir import Device, Label, PlcProject, ProgramUnit
from plcxray.report import report_json, report_markdown


def test_report_json():
    project = PlcProject(
        path="test.gxw",
        project_name="test",
        format="GX Works project container",
        sha256="abc123",
        file_size=1024,
        streams=["ProjectInfo"],
        pous=[ProgramUnit(name="Main", kind="program")],
        devices=[Device(name="M0")],
        labels=[Label(name="START")],
    )
    report = report_json(project)
    assert "test" in report
    assert "abc123" in report


def test_report_markdown():
    project = PlcProject(
        path="test.gxw",
        project_name="test",
        format="GX Works project container",
        sha256="abc123",
        file_size=1024,
        streams=["ProjectInfo"],
        pous=[ProgramUnit(name="Main", kind="program")],
        devices=[Device(name="M0")],
        labels=[Label(name="START")],
    )
    report = report_markdown(project)
    assert "# PLC-XRAY Inspection Report" in report
    assert "test" in report
    assert "GX Works project container" in report
