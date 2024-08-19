from glob import glob
from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, ParallelCompile


ext_modules = [
    Pybind11Extension(
        "example_package_1_bnprks.cpp",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
        extra_compile_args = [
            "-std=c++17"
        ]
    ),
]


setup(
    ext_modules=ext_modules,
)
