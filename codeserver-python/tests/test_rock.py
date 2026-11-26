# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess

import pytest


def test_pebble_services(rock_container):
    """Test the codeserver-jupyter service."""
    rock_services = rock_container[0].get_services()

    # verify rock service
    assert rock_services["codeserver-jupyter"]
    assert rock_services["codeserver-jupyter"]["startup"] == "enabled"


@pytest.mark.parametrize(
    "path", ["/usr/bin/code-server", "/opt/conda/bin/jupyter"]
)
def test_artifacts(rock_container, path):
    """Test that an artifact is in its correct location."""
    # -L follows symlinks, so a dangling link fails too
    subprocess.run(
        ["docker", "exec", rock_container[1], "ls", "-L", path],
        check=True,
    )
