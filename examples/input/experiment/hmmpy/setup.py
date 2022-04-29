import os
from setuptools import setup, Extension

# Set local env var CYTHON = True if working with Cython vackend
# Assumes (for now) pyodide if not CYTHON
CYTHON = os.environ.get("CYTHON", False)

if CYTHON:
    from Cython.Build import cythonize  # noqa

    setup(
        name='hmmpy',
        version='0.1',
        packages=['hmmpy'],
        ext_modules=cythonize("chmmpy.pyx"),
    )
else:
    setup(
        name='hmmpy',
        version='0.1',
        packages=['hmmpy'],
        ext_modules = [Extension(name = "chmmpy", sources = ["hmmpy/chmmpy.c"])]
    )
