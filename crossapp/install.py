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
        os.makedirs(VIRTUALENV_DIR)
    

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

# Installation control.
class Install:
    """
    Installation class.
    """

    # Initialize the installation.
    def __init__(self, crossapp_dir = CROSSAPP_DIR, virtualenv_dir = VIRTUALENV_DIR, database_dir = DATABASE_DIR, database_file = DATABASE_FILE):
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
    
    # Install the application from repository.
    def install_from_repo(self, appid, repo):
        """
        Install the application from repository.
        """
        pass