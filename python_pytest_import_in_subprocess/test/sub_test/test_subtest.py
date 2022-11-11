import logging
import os
import pytest
import subprocess
import sys

from test.sub_test.sub_test_lib import sub_test_string


@pytest.fixture
def subprocess_logs():
    cmd = [sys.executable, os.path.dirname(__file__) + "/subprocess_script.py"]
    subprocess_result = subprocess.run(
        cmd,
        text=True,
        capture_output=True
    )
    try:
        subprocess_result.check_returncode()
    except subprocess.CalledProcessError as exc:
        logging.error(
            "Failed subprocess call with return code %s\nstderr: %s\nstdout: %s",
            subprocess_result.returncode,
            subprocess_result.stderr,
            subprocess_result.stdout
        )
        raise exc

    return subprocess_result.stdout


def test_subprocess_log(subprocess_logs):
    assert sub_test_string in subprocess_logs
