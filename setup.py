#!/usr/bin/env python
"""
spreadsheet-importer
==============

The small library is meant to reduce the parsing of csv, xls and xlsx files and extract an array content.

:copyright: (c) 2012 by the Linovia, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
    # 'nose==1.1.2',
]

install_requires = [
    'xlrd',
    'openpyxl',
]

setup(
    name='spreadsheet-importer',
    version='0.0.1',
    author='Xavier Ordoquy',
    author_email='xordoquy@linovia.com',
    url='http://github.com/linovia/spreadsheet-importer',
    description='A csv, xls and xlsx data array parser',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
