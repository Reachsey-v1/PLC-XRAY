from plcxray.ir import Device, Evidence, Label, PlcProject, ProgramUnit
import json


def test_ir_objects_build():
    project = PlcProject(
        path="sample.gxw",
        project_name="sample",
        format="GX Works project container",
        sha256="abc",
        file_size=123,
        streams=["ProjectInfo"],
        pous=[ProgramUnit(name="Main", kind="program")],
        devices=[Device(name="M0")],
        labels=[Label(name="START")],
        evidence=[Evidence(source="scanner", item="labels", detail="one label discovered", confidence="low")],
    )
    payload = project.to_dict()
    assert payload["project_name"] == "sample"
    assert payload["pous"][0]["name"] == "Main"
    assert payload["devices"][0]["name"] == "M0"
    assert payload["evidence"][0]["source"] == "scanner"


def test_ir_serialization():
    project = PlcProject(
        path="sample.gxw",
        project_name="sample",
        format="GX Works project container",
        sha256="abc",
        file_size=123,
    )
    payload = project.to_dict()
    serialized = json.dumps(payload)  # Should not raise
    assert "sample" in serialized
