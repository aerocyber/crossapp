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

from . import *
import click

version = __version__.Version

# CUI Interface with click module

@click.group()
@click.version_option(version=version)
def cli():
    pass

@cli.command()
@click.option('--install', help='Install app from cap file', default=False)
@click.argument('capfile', type=click.Path(exists=True), required=False)
# @click.option("--from-repo", "-e", help="Install app from repo", default=False)
# @click.argument('repo', type=click.STRING)
@click.option('--uninstall', help='Uninstall app',  default=False)
@click.argument('appname', type=click.STRING)
@click.option('--remove-repo', '-d', help='Remove repo',  default=False)
@click.argument('repo_name', type=click.STRING)
@click.option('--list-all', help='List installed apps', default=False)
@click.option('--update', help='Update installed apps', default=False)
@click.option('--version', help='Show version', default=True)



def main():
    """
    CrossApp is a cross-platform application framework.
    """
    pass

if __name__ == '__main__':
    main()
