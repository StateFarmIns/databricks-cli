# Databricks CLI
# Copyright 2017 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"), except
# that the use of services to which certain application programming
# interfaces (each, an "API") connect requires that the user first obtain
# a license for the use of the APIs from Databricks, Inc. ("Databricks"),
# by creating an account at www.databricks.com and agreeing to either (a)
# the Community Edition Terms of Service, (b) the Databricks Terms of
# Service, or (c) another written agreement between Licensee and Databricks
# for the use of the APIs.
#
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib.util
import os
import sys

from setuptools import setup, find_packages

# Get version
# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
# We do this because this is executed before it is installed
module_name = "databricks_cli.version"
spec = importlib.util.spec_from_file_location(
    module_name, os.path.join('databricks_cli', 'version.py')
)

if spec is None:
    raise ValueError('Install failed, could not fild databricks_cli.version module.')

databricks_cli_version = importlib.util.module_from_spec(spec)
sys.modules[module_name] = databricks_cli_version
spec.loader.exec_module(databricks_cli_version)
version = databricks_cli_version.version

# Prevent open file handles leaking
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='databricks-cli',
    version=version,
    packages=find_packages(include=['databricks_cli*']),
    install_requires=[
        # Note: please keep this in sync with `requirements.txt`.
        'click>=7.0',
        'pyjwt>=1.7.0',
        'oauthlib>=3.1.0',
        'requests>=2.17.3',
        'tabulate>=0.7.7',
        'six>=1.10.0',
        'configparser>=0.3.5;python_version < "3.6"',
        'urllib3>=1.26.7,<2.0.0',
    ],
    entry_points='''
        [console_scripts]
        databricks=databricks_cli.cli:main
        dbfs=databricks_cli.dbfs.cli:dbfs_group
    ''',
    zip_safe=False,
    author='Andrew Chen',
    author_email='andrewchen@databricks.com',
    description='A command line interface for Databricks',
    long_description=long_description,
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
    ],
    keywords='databricks cli',
    url='https://github.com/databricks/databricks-cli',
    options={'bdist_wheel': {'universal': True}},
)
