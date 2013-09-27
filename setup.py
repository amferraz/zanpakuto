# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="zanpakuto",
    version='0.1',
    author="Anderson Ferraz",
    author_email="amarquesferraz@gmail.com",
    description="A small utility to simplify HTML excerpts",
    url="https://github.com/amferraz/zanpakuto",
    download_url='https://github.com/amferraz/zanpakuto/archive/0.1.zip',
    packages=['zanpakuto'],
    install_requires=['lxml==3.2.3'],
)
