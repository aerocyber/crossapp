#!usr/bin/env python3
# -*- coding: utf-8 -*-


# Copyright 2021 aerocyber
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()
setuptools.setup(
    name="crossapp",
    version="1.0.0",
    author="aerocyber",
    author_email=None,
    description="A small wrapper for Python's zipapp module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aerocyber/crossapp",
    project_urls={
        "Bug Tracker": "https://github.com/aerocyber/crossapp/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "crossapp = crossapp.__main__:main",
        ],
    },
    install_requires=requirements,
)
