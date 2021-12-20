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

HOME = os.path.expanduser("~")
APPINFO = os.path.join(HOME, '.crossapp', 'apps.json')

def install(cap_path):
    # Read from the json file
    f = open(cap_path, 'r')
    cap = json.load(f)
    f.close()
    
    # Read the app.json file
    g = open(APPINFO, 'r')
    apps = json.load(g)
    g.close()
    
    # Get the property appId from the cap file
    appId = cap['appId']
    
    # Check if the appId is already in the apps.json file
    if appId in apps["Installed"]["appId"]:
        # Check for version match
        if apps[appId]["version"] == cap["version"]:
            return {"Status": "error", "Detail": "The app is already installed"}
        
        # If version to be installed is newer than the installed version, replace the installed version
        if cap["version"] > apps[appId]["version"]:
            INSTDIR = apps[appId]["installDir"]
            INSTPATH = os.path.join(INSTDIR, (appId + apps["version"] + '.pyz'))
            os.remove(INSTPATH)
        
        # If version to be installed is older than the installed version, return error
        if cap["version"] < apps[appId]["version"]:
            return {"Status": "error", "Detail": "The app is already installed"}
    
    else:
        INSTDIR = os.path.join(HOME, 'crossapp', 'installations', 'apps', appId)
        INSTPATH = os.path.join(INSTDIR, (appId + cap["version"] + '.pyz'))
    
    data = cap["Data"]
    
    # Write the data to INSTPATH
    f = open(INSTPATH, 'w')
    f.write(data)
    f.close()
    
    # Update apps and write to apps.json
    apps["Installed"]["appId"].append(appId)
    dat = {
        "version": cap["version"],
        "installDir": INSTDIR, 
        "appName": cap["appName"],
        "repo": cap["repo"],
        "author": cap["author"],
        "website": cap["website"],
        }
    
    apps[appId] = dat
    f = open(APPINFO, 'w')
    json.dump(apps, f)
    f.close()
    
    return {"Status": "success", "Detail": "The app is installed"}