#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='text_data_cards',
    version='0.1.0',
    description="Utility module for working with text data with a "
                "line-oriented format, especially fixed-width or "
                "Fortran-format records.",
    long_description=readme + '\n\n' + history,
    author="Paul David Brown",
    author_email='pdb.lists@gmail.com',
    url='https://github.com/pdb5627/text_data_cards',
    packages=[
        'text_data_cards',
    ],
    package_dir={'text_data_cards':
                 'text_data_cards'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='text_data_cards',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
