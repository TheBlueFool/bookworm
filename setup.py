#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

from setuptools import find_packages, setup

__version__ = "0.1dev"


setup(
    name="bookworm",
    version=__version__,
    description="Shakespeare",
    author="NA",
    url="https://github.com/TheBlueFool/bookworm",
    packages=find_packages("flaskr"),
    package_dir={"": "src"},
    author_email="richard.pavis@gmail.com",
    long_description=open("README.md").read(),
)
