#-*- coding:utf8 -*-
from setuptools import setup, find_packages

setup(
    name="example04",
    version="1.0.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
    # , py_modules=['example04','example04.hello']
)