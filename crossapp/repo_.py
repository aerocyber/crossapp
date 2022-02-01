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

#### About ####
# This script is used to add a new repository to the list of repositories
# that will be used for app installation and updation.
#### End ####

#### Imports ####
from . import install
import os
import requests
import json
# import pickle
#### End ####

#### Constants ####
# The location of the file that contains the list of repositories
REPO_LIST_FILE = os.path.join(
    install.CROSSAPP_DIR, 'repositories', "repos.db")
#### End ####


#### Functions ####
def create_repo_dir():
    """
    Create the directory that contains the repository.
    """
    if not os.path.exists(os.path.join(install.CROSSAPP_DIR, "repositories")):
        os.makedirs(os.path.join(install.CROSSAPP_DIR, "repositories"))


def create_repo_list_file():
    """
    Create the file that contains the list of repositories.
    """
    if not os.path.exists(REPO_LIST_FILE):
        with open(REPO_LIST_FILE, 'wb') as f:
            f.write("{}")


#### End ####

#### Classes ####
class RepoExistanceError(Exception):
    """
    An exception that is raised when a repository is already in the list of
    repositories.
    """
    pass


class repoManagement:
    """
        A class for managing repositories.
    """

    def __init__(self, url, name):
        self._url = url
        self._name = name
        create_repo_dir()
        create_repo_list_file()

    def add_repo(self):
        """
            Add the repository if not exists.
        """
        with open(REPO_LIST_FILE, 'rb') as f:
            repo_list = json.load(f)
        for x in repo_list:
            if x['url'] == self._url:
                raise RepoExistanceError("Repository already exists.")
        repo_list.append({'url': self._url, 'name': self._name})
        with open(REPO_LIST_FILE, 'wb') as f:
            json.dump(repo_list, f)
        return True  # Indicate that the repository was added successfully.

    def remove_repo(self):
        """
            Remove the repository if exists.
        """
        with open(REPO_LIST_FILE, 'rb') as f:
            repo_list = json.load(f)
        for x in repo_list:
            if x['url'] == self._url:
                repo_list.remove(x)
                with open(REPO_LIST_FILE, 'wb') as f:
                    json.dump(repo_list, f)
                return True
        raise RepoExistanceError("Repository does not exist.")

    def update_repo(self):
        """
            Replace the repo with the new one.
        """
        with open(REPO_LIST_FILE, 'rb') as f:
            repo_list = json.load(f)
        for x in repo_list:
            if x['name'] == self._name:
                repo_list.remove(x)
                repo_list.append({'url': self._url, 'name': self._name})
                with open(REPO_LIST_FILE, 'wb') as f:
                    json.dump(repo_list, f)
                return True
        raise RepoExistanceError("Repository does not exist.")


#### End ####
