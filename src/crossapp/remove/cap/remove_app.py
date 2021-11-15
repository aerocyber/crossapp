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

# Import libraries
import os
import json
from crossapp.remove.cap import remove_app

# Constants
HOME = os.path.expanduser("~")
APPINFO = os.path.join(HOME, '.crossapp', 'apps.json')

def remove_list(app_list):
    """Remove a list of apps"""
    for app in app_list:
        _ = remove_app(app)
    return _

def remove_app(appId):
    # Load the installed apps
    f = open(APPINFO, 'r')
    apps = json.load(f)
    f.close()

    # Remove the app
    appLoc = apps[installDir]
    os.remove(appLoc)
    del apps[appId]
    return {'Status': 'Success'}
