import os
from glob import glob
from setuptools import setup

import platform

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension

include_dirs = ["src/"]
library_dirs = []
libraries = ["hdf5", "hwy"]

if platform.system() == "Windows":
    extra_compile_args = ["/std:c++17"]
    libraries.append("zlib")
    # Mimic the unix compiler environment variable settings
    if "CPATH" in os.environ:
        include_dirs.extend(os.environ["CPATH"].split(";"))
    if "LIBRARY_PATH" in os.environ:
        library_dirs.extend(os.environ["LIBRARY_PATH"].split(";"))
else:
    extra_compile_args = ["-std=c++17"] 
    libraries.append("z")
    # Mimic the unix compiler environment variable settings
    if "CPATH" in os.environ:
        include_dirs.extend(os.environ["CPATH"].split(":"))
    if "LIBRARY_PATH" in os.environ:
        library_dirs.extend(os.environ["LIBRARY_PATH"].split(":"))

if "CPATH" in os.environ:
    print(f"CPATH={os.environ['CPATH']}")
else:
    print("CPATH not set")

if "LIBRARY_PATH" in os.environ:
    print(f"LIBRARY_PATH={os.environ['LIBRARY_PATH']}")
else:
    print("LIBRARY_PATH not set") 

ext_modules = [
    Pybind11Extension(
        "example_package_1_bnprks.cpp",
        sorted(glob("src/*.cpp")),  # Sort source files for reproducibility
        extra_compile_args = extra_compile_args,
        libraries = libraries,
        include_dirs = include_dirs,
        library_dirs = library_dirs,
    ),
]


setup(
    ext_modules=ext_modules,
)
