from setuptools import setup, find_packages

from epythonsetuptools.tools import setup as epythonsetup, entrypoint

setup(
    **epythonsetup(
        name="change",
        version='0.1',
        install_requires=["click"],
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        entry_points=entrypoint("click", "shell", "change=change.app:main"),
    )
)
