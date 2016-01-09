#!/usr/bin/env python

from setuptools import setup

setup(
    name='hipcat',
    version='0.0.1',
    description='Pipe text to HipChat',
    author='Mark Smith',
    author_email='judy@judy.co.uk',
    url='https://www.github.com/judy2k/hipcat/',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications :: Chat",
    ],

    packages=['hipcat'],
    install_requires=[
        "click>=4.0",
        "requests",
    ],
    entry_points='''
        [console_scripts]
        hipcat=hipcat.cli:main
    ''',
)

