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
# This script is used to install the application from repository or a .cap file.
# It will create a virtualenv, if already not present, and install the application.
# It will also create a database, if already not present.
#### End ####

#### Imports ####
import os
import requests
from . import envCreate
import pickle
import json
import shutil
#### End ####

#### Constants ####
# User's home directory
HOME_DIR = os.path.expanduser("~")
# CrossApp directory
CROSSAPP_DIR = os.path.join(HOME_DIR, ".crossapp")
# Virtualenv directory
VIRTUALENV_DIR = os.path.join(CROSSAPP_DIR, "virtualenv")
# Database directory
DATABASE_DIR = os.path.join(CROSSAPP_DIR, "database")
# Database file
DATABASE_FILE = os.path.join(DATABASE_DIR, "crossapp.db")
#### End ####


#### Functions ####

# Create CrossApp directory
def create_crossapp_dir():
    """
    Create the CrossApp directory if not exists already.
    """
    if not os.path.exists(CROSSAPP_DIR):
        os.makedirs(CROSSAPP_DIR)

# Create virtualenv directory


def create_virtualenv_dir():
    """
    Create the virtualenv directory if not exists already.
    """
    if not os.path.exists(VIRTUALENV_DIR):
        env = envCreate.createEnv(VIRTUALENV_DIR)
        env.create_virtual_env()


# Create database directory
def create_database_dir():
    """
    Create the database directory if not exists already.
    """
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)

# Create database file


def create_database_file():
    """
    Create the database file if not exists already.
    """
    if not os.path.exists(DATABASE_FILE):
        open(DATABASE_FILE, "w").close()

#### End ####

#### Classes ####

# Error


class AppNotFound(Exception):
    """
    Exception class for AppNotFound.
    """
    pass


class AppAlreadyInstalled(Exception):
    """
    Exception class for AppAlreadyInstalled.
    """
    pass

# Installation control.


class Install:
    """
    Installation class.
    """

    # Initialize the installation.
    def __init__(self, crossapp_dir=CROSSAPP_DIR, virtualenv_dir=VIRTUALENV_DIR, database_dir=DATABASE_DIR, database_file=DATABASE_FILE):
        """
        Initialize the installation.
        """
        # Create CrossApp directory
        create_crossapp_dir()
        # Create virtualenv directory
        create_virtualenv_dir()
        # Create database directory
        create_database_dir()
        # Create database file
        create_database_file()

    def get_installed_apps(self):
        """
        Get the list of installed apps.
        """
        f = open(DATABASE_FILE, "rb")
        db = pickle.load(f)
        f.close()
        return db  # Return the list of installed apps.

    def remove_app(self, appid, removeDataDir=False):
        """
            Remove the application.
        """
        f = open(DATABASE_FILE, "rb")
        db = pickle.load(f)
        f.close()
        if appid in db:
            loc = db[appid]["Location"]
        else:
            return AppNotFound("App not installed.")

        if removeDataDir:
            shutil.rmtree(loc)
            del db[appid]
        else:
            del db[appid]
            # Delete the pyz file.
            os.remove(os.path.join(loc, db[appid]["Name"] + '.pyz'))
        f = open(DATABASE_FILE, "wb")
        pickle.dump(db, f)
        f.close()
        return True  # Indicate successful operation.

    # Install the application from repository.
    def install_from_repo(self, appid, repo):
        """
           Install the application from repository.

           Args:
                appid (str): The application ID.
                repo (str): The repository URL.

            Returns:
                bool: True if the installation is successful.

            Exception:
                AppNotFound: If the application is not found in repo.
        """
        repo_get = requests.get(repo)  # Get repository
        repo_get.raise_for_status()  # Raise exception if error
        if repo_get.status_code == 200:
            # Continue.
            apps = repo_get.json()  # Get the JSON data
            if appid in apps:
                # Continue.
                app = apps[appid]
            else:
                # Raise exception.
                raise AppNotFound(
                    "Application not found in {repourl}".format(repourl=repo))
            # Check if app is already installed.
            apps_installed = self.get_installed_apps()
            if appid in apps_installed:
                if app["version"] == apps_installed[appid]["version"]:
                    # App already installed.
                    raise AppAlreadyInstalled("App already installed.")
                else:
                    # Remove already installed app.
                    self.remove_app(appid)

            # Install the application.
            # Write the application's name to the database.
            f = open(DATABASE_FILE, "rb")
            db = pickle.load(f)
            f.close()
            db[appid] = {
                "Name": app["name"],
                "Repo": repo,
                "Version": app["version"],
                "Author": app["author"],
                "Description": app["description"],
                "Website": app["website"],
                "License": app["license"],
                "Location": os.path.join(CROSSAPP_DIR, "Apps", appid)
            }
            f = open(DATABASE_FILE, "wb")
            pickle.dump(db, f)
            f.close()
            # Create the application's directory.
            if not os.path.exists(os.path.join(CROSSAPP_DIR, "Apps", appid)):
                os.makedirs(os.path.join(CROSSAPP_DIR, "Apps", appid))
            # Write the application's code to the directory.
            f = open(os.path.join(CROSSAPP_DIR, "Apps",
                     appid, app["Name"] + '.pyz'), 'wb')
            f.write(app["Data"])
            f.close()
            return True  # Indicate successful operation.

    def install_from_cap(self, cap_file_path):
        """
            Install app from cap file.
        Args:
            cap_file_path (str): Path to cap file.
        """
        if not os.path.exists(cap_file_path):
            raise FileNotFoundError("Cap file not found.")

        # Read cap file.
        with open(cap_file_path, "r") as f:
            cap = json.load(f)

        # Check if app is already installed.
        installed_apps = self.get_installed_apps()
        if cap["appid"] in installed_apps:
            if cap["version"] == installed_apps[cap["appid"]]["version"]:
                # App already installed.
                raise AppAlreadyInstalled("App already installed.")
            else:
                # Remove already installed app.
                self.remove_app(cap["appid"])

        # Install the application.
        # Write the application's name to the database.
            f = open(DATABASE_FILE, "rb")
            db = pickle.load(f)
            f.close()
            db[cap["appid"]] = {
                "Name": cap["name"],
                "Repo": cap["repo"],
                "Version": cap["version"],
                "Author": cap["author"],
                "Description": cap["description"],
                "Website": cap["website"],
                "License": cap["license"],
                "Location": os.path.join(CROSSAPP_DIR, "Apps", cap["appid"])
            }
            f = open(DATABASE_FILE, "wb")
            pickle.dump(db, f)
            f.close()
            # Create the application's directory.
            if not os.path.exists(os.path.join(CROSSAPP_DIR, "Apps", cap["appid"])):
                os.makedirs(os.path.join(CROSSAPP_DIR, "Apps", cap["appid"]))
            # Write the application's code to the directory.
            f = open(os.path.join(CROSSAPP_DIR, "Apps",
                     cap["appid"], cap["Name"] + '.pyz'), 'wb')
            f.write(cap["Data"])
            f.close()
            return True  # Indicate successful operation.
