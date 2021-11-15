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


# Standard library
import os
import pickle
import requests

# Constants
HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, ".crossapp", "repos.list")

def install(appId):
    # Read the repo list
    f = open(REPO, "rb")
    repos = pickle.load(f)
    f.close()

    # Download the app from the repo using requests and save it to the temp directory of the user at HOME/tmp/
    flag = 0
    for url in repos.values():
        r = requests.get(url)
        if appId in r.json():
            flag = 1
            # Download the app
            f = open(os.path.join(HOME, "tmp", appId + ".cap"), "wb")
            s = requests.get(r.json()[appId])
            f.write(s.content)
            f.close()
            break
    if flag == 0:
        return {"status": "Fail", "message": "App not found in repo"}
    else:
        from crossapp.add.cap import install_cap
        ret = install_cap.install(os.path.join(HOME, "tmp", appId + ".cap"))
        if ret["Status"] == "Success":
            # Write the app and repoName to the list that is saved in the installation directory
            f = open(os.path.join(HOME, ".crossapp", "installed.list"), "rb")
            data = pickle.load(f)
            f.close()
            data[appId] = url
            f = open(os.path.join(HOME, ".crossapp", "installed.list"), "wb")
            pickle.dump(data, f)
            f.close()
        # Remove the temporary file
        os.remove(os.path.join(HOME, "tmp", appId + ".cap"))
        return ret
