#!/usr/bin/env python

from setuptools import setup, find_packages
import sys


long_description = "Pipe text to HipChat"
try:
    long_description = open("README.rst").read()
except Exception as e:
    print(e, file=sys.stderr)


setup(
    name='hipcat',
    version='0.0.10',
    description='Pipe text to HipChat',
    long_description=long_description,
    author='Mark Smith',
    author_email='judy@judy.co.uk',
    url='https://www.github.com/judy2k/hipcat/',
    license="GNU General Public License v2 (GPLv2)",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Communications :: Chat",
    ],
    platforms='any',

    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "click>=4.0",
        "requests",
    ],
    entry_points='''
        [console_scripts]
        hipcat=hipcat.cli:main
    ''',
)
