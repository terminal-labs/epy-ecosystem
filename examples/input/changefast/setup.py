from setuptools import setup, find_packages
from epythonsetuptools.tools import setup as epythonsetup, entrypoint

setup(
    **epythonsetup(
        name="changefast",
        version="0.0.0",
        install_requires=["click"],
        packages=find_packages(),
        include_package_data=True,
        entry_points=entrypoint("click", "shell", "changefast=changefast.app:main"),
    )
)
