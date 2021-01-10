from setuptools import setup

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext

import sys

__version__ = "0.0.1"

# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

zlib_dir = 'src/zlib-1.2.11/'
zlib_sources = [zlib_dir + fn for fn in ['adler32.c', 'compress.c', 'crc32.c', 'deflate.c', 'gzclose.c', 'gzlib.c', 'gzread.c', 'gzwrite.c', 'infback.c', 'inffast.c', 'inflate.c', 'inftrees.c', 'trees.c', 'uncompr.c', 'zutil.c']]

ext_modules = [
    Pybind11Extension("pyspng",
        ["src/main.cpp", "src/libspng-0.6.1/spng/spng.c"] + zlib_sources,
        include_dirs=['src/libspng-0.6.1', zlib_dir],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        libraries=['z'],
    ),
]

setup(
    name="pyspng",
    version=__version__,
    author="Janne Hellsten",
    author_email="jjhellst@gmail.com",
    url="https://github.com/nurpax/pyspng", # TODO
    description="Minimal binding for libspng",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    install_requires=[
        'numpy',
    ],
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
