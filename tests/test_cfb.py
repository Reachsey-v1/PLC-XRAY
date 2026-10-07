import json
import subprocess
import sys


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "plcxray.cli", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "PLC-XRAY" in result.stdout


def test_cli_json_output(tmp_path):
    project_path = tmp_path / "sample.gxw"
    project_path.write_bytes(b"PLC-XRAY-FAKE-GXW")
    result = subprocess.run(
        [sys.executable, "-m", "plcxray.cli", "inspect", str(project_path), "--json"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["project_name"] == "sample"
    assert payload["format"]
