from setuptools import setup, find_packages

setup(
    name="example02",
    version="1.0.1",
    # packages=find_packages(where='lib'),
    package_dir={'': 'lib'},
    py_modules=['example02',]
)