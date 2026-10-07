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
    assert project.to_dict()["path"] == "sample.gxw"
    assert project.pous[0].name == "Main"
