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
