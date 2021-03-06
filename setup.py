#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2019 Luciano Resende
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'click>=6.0',
    'bumpversion>=0.5.3',
    'wheel>=0.30.0',
    'watchdog>=0.8.3',
    'flake8>=3.5.0',
    'tox>=2.9.1',
    'coverage>=4.5.1',
    'twine>=1.10.0',
    'requests >= 2.8, < 3.0',
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Luciano Resende",
    author_email='lresende@apache.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Fabric for Deep Learning python client.",
    install_requires=requirements,
    license='Apache License, Version 2.0',
    long_description=readme,
    include_package_data=True,
    keywords=['ffdl', 'client'],
    name='ffdl-client',
    packages=find_packages(include=['ffdl', 'ffdl.client']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lresende/ffdl-python-client',
    version='0.1.2',
    zip_safe=False,
)
