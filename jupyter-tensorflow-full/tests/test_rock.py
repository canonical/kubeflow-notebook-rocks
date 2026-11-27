# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess


def test_pebble_services(rock_container):
    """Test the jupyter service and binary."""
    rock_services = rock_container[0].get_services()

    # verify rock service
    assert rock_services["jupyter"]
    assert rock_services["jupyter"]["startup"] == "enabled"

    # verify that artifacts are in correct locations
    subprocess.run(
        [
            "docker",
            "exec",
            rock_container[1],
            "ls",
            "/opt/conda/bin/jupyter",
        ],
        check=True,
    )

