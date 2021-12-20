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

# Imports


import click
from crossapp.add.cap import install_cap
from crossapp.add.repo import install as install_from_repo
from crossapp.add.repo import repoMgmt
from crossapp.create import build as buildcap
from crossapp.create import createDirStruc
from crossapp.list import search
from crossapp.remove.repo import remove_repo
from crossapp.remove.cap import remove_app
from . import __version__


# Constants


INFO = """
CrossApp
version: {}
A framework for building cross-platform open source applications in Python.
""".format(__version__.Version)


# CUI


# Install group


@click.group()
def install_fns():
    pass


@click.command()
@click.option('--repo', '-r', default=False, help='Repo to install from')
@click.option('--cap', '-c', default=True, help='Cap to install')
@click.argument('Appid')
def install(repo, cap, Appid):
    if repo:
        install_from_repo(Appid)
    elif cap:
        install_cap(Appid)
    else:
        click.echo("No options selected")


install_fns.add_command(install)


@click.command()
@click.argument('repoUrl')
@click.argument('repoName')
def add_repo(repoUrl, repoName):
    repoMgmt.add(repoName, repoUrl)


install_fns.add_command(add_repo)


# Uninstall group


@click.group()
def remove_fns():
    pass


@click.command()
@click.argument('repoName')
def remove_repo_cmd(repoName):
    remove_repo(repoName)


remove_fns.add_command(remove_repo_cmd)


@click.command()
@click.argument('Appid')
def remove_app_cmd(Appid):
    remove_app(Appid)


remove_fns.add_command(remove_app_cmd)


def main():
    pass


if __name__ == '__main__':
    main()
