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
# This script is used to create the virtual environment with which Apps are to be used.
# This acts as an isolated Python so as not to interfere with the existing Python.
# This, however does not downloads a new Python interpreter.
#### End ####

#### Imports ####
import os
import venv
#### End ####

#### Classes ####


class createEnv:
    """
    Create the virtual environment with which Apps are to be used.
    """

    def __init__(self, Path_to_env):
        """
        Initialize the class with the name of the application.
        """
        self.path = Path_to_env

    def create_virtual_env(self):
        """
           Use Python's venv module for environment creation.
        """
        if not os.path.exists(os.path.join(self.path, "bin")):
            venv.create(
                os.path.normpath(os.path.normcase(self.path)),
                with_pip=False,
                symlinks=False
            )


#### End ####
