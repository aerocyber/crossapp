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

import os
from json import loads

HOME = os.path.expanduser("~")
APPINFO = os.path.join(HOME, '.crossapp', 'apps.json')


def checkAppId(appname):
    """
    Check if the appid is present in APPINFO
    """
    f = open(APPINFO, 'r')
    apps = loads(f.read())
    f.close()
    
    if appname in apps["Installed"]["appName"]:
        return {
            "Status": "Success",
            "Detail": appname + " is installed"
        }
    
    else:
        return {
            "Status": "Failure",
            "Detail": appname + " is not installed"
        }