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

import click
from getpass import getuser
from crossapp.add.cap import install_cap
from crossapp.add.repo import install as instFromRepo
from crossapp.add.repo import repoMgmt
from crossapp.create import build as buildcap
from crossapp.create import createDirStruc
from crossapp.list import search
from crossapp.remove.repo import remove_repo
from crossapp.remove.cap import remove_app
from . import __version__

# The interface design


@click.group()
def main():
    """
    The main function.
    """
    click.echo(f"Welcome to CrossApp, {getuser()}!")


@main.group()
def create():
    """
    Create a new CrossApp project directory structure.
    """
    pass


@main.group()
def build():
    """
    Build a CrossApp project.
    """
    pass


@main.group()
def install():
    """
    Install a crossapp application from a cap file.
    """
    pass


@main.group()
def add():
    """
    Install a crossapp application from a repository.
    """
    pass


@main.group()
def repo():
    """
    Add a new repository.
    """
    pass


@main.group()
def removerep():
    """
    Remove a crossapp repository.
    """
    pass


@main.group()
def search():
    """
    Search for a crossapp application.
    """
    pass


@main.group()
def uninstall():
    """
    Uninstall a crossapp application.
    """
    pass


@main.group()
def Version():
    """
    Show the version of CrossApp.
    """
    pass


@main.group()
def instfromrepos():
    """
    Install a crossapp application from a repository.
    """
    pass


@click.command()
@click.argument('appname')
def searchapp(appname):
    """
    Search for a crossapp application.
    """
    result = search.checkAppId(appname)
    click.echo(result["Detail"])


@click.command()
@click.argument('cap_file', type=click.Path(exists=True))
def installcap(cap_file):
    """
    Install a crossapp application from a cap file.
    """
    result = install_cap.install(cap_file)
    click.echo(result["Detail"])


@click.command()
@click.argument('repo_name')
@click.argument('repo_url')
def addrepo(repo_name, repo_url):
    """
    Add a new repository.
    """
    result = repoMgmt.add(repo_name, repo_url)
    click.echo(result["Detail"])


@click.command()
@click.argument('repo_name')
def removerepo(repo_name):
    """
    Remove a repository.
    """
    result = repoMgmt.remove(repo_name)
    click.echo(result["Detail"])


@click.command()
@click.argument('appname')
def remove(appname):
    """
    Uninstall a crossapp application.
    """
    result = remove_app.remove_app(appname)
    click.echo(result["Detail"])


@click.command()
def version():
    """
    Show the version of CrossApp.
    """
    click.echo(__version__)


@click.command()
@click.argument('appname')
def buildcap(appname):
    """
    Build a crossapp application.
    """
    result = buildcap.build(appname)
    click.echo(result["Detail"])


@click.command()
@click.argument('appname')
def createdir(appname):
    """
    Create a new CrossApp project directory structure.
    """
    result = createDirStruc.create(appname)
    click.echo(result["Detail"])


@click.command()
@click.argument('appId')
def instfromrepo(appId):
    """
    Install a crossapp application from a repository.
    """
    result = instFromRepo.install(appId)
    click.echo(result["Detail"])


create.add_command(createdir)
build.add_command(buildcap)
install.add_command(installcap)
add.add_command(addrepo)
repo.add_command(addrepo)
removerep.add_command(removerepo)
search.add_command(searchapp)
uninstall.add_command(remove)
Version.add_command(version)
instfromrepos.add_command(instfromrepo)


if __name__ == '__main__':
    main()
