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
import json

HOME = os.expanduser("~")
APPINFO = os.path.join(HOME, '.crossapp', 'apps.json')

def getStorageLocation(appId):
    f_apps = open(APPINFO)
    apps = json.load(f_apps)
    f_apps.close()
    if (appId in apps["Installed"]["By Id"]):
        INSTPATH = apps[appId]["Installed Path"]
        STORAGE = os.path.join(INSTPATH, 'Storage')
        return {"Status": "Success", "Detail": str(STORAGE)}
    else:
        return {"Status": "Fail", "Detail": "Storage API currently supports ONLY installed apps."}

