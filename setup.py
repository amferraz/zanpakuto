# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="zanpakuto",
    version='0.1',
    author="Anderson Ferraz",
    author_email="amarquesferraz@gmail.com",
    description="A small utility to simplify HTML excerpts",
    url="https://github.com/amferraz/zanpakuto",
    packages=find_packages(),
    install_requires=['lxml==3.2.3']
)
