from plcxray.ir import Device, Label, PlcProject, ProgramUnit


def test_ir_objects_build():
    project = PlcProject(
        path="sample.gxw",
        format="GX Works project container",
        sha256="abc",
        file_size=123,
        streams=["ProjectInfo"],
        pous=[ProgramUnit(name="Main", kind="program")],
        devices=[Device(name="M0")],
        labels=[Label(name="START")],
    )
    payload = project.to_dict()
    assert payload["path"] == "sample.gxw"
    assert payload["pous"][0]["name"] == "Main"
    assert payload["devices"][0]["name"] == "M0"
