# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess

import pytest


@pytest.mark.parametrize(
    "module",
    [
        # Jupyter packages
        "jupyterlab",
        "notebook",
        "ipykernel",
        # SciPy ecosystem packages
        "altair",
        "bokeh",
        "bottleneck",
        "brotli",
        "cloudpickle",
        "dask",
        "dill",
        "h5py",
        "ipympl",
        "ipywidgets",
        "jupyterlab_git",
        "matplotlib",
        "numba",
        "numexpr",
        "openpyxl",
        "pandas",
        "patsy",
        "scipy",
        "seaborn",
        "sqlalchemy",
        "statsmodels",
        "sympy",
        "tables",
        "vincent",
        "xlrd",
        # Machine Learning & Data Science
        "sklearn",
        "mlflow",
        "feast",
        # NumPy linked against OpenBLAS
        "numpy",
        "scipy.linalg",
    ],
)
def test_import(rock_container, module):
    """Test that a Python module imports in the rock's conda env."""
    subprocess.run(
        [
            "docker",
            "exec",
            "-e",
            "HOME=/home/jovyan",
            "-e",
            "PYTHONPATH=/opt/conda/lib/python3.11/site-packages/",
            rock_container[1],
            "/opt/conda/bin/python3",
            "-c",
            f"import {module}",
        ],
        check=True,
    )
