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
import pickle
from crossapp.remove.cap import remove_app

# Constants
HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, ".crossapp", "repos.list")
INSTALLED = os.path.join(HOME, ".crossapp", "installed.list")
APPINFO = os.path.join(HOME, '.crossapp', 'apps.json')

def remove_repo(repo_name):
    """
    Remove a repository from the list of repositories.
    """
    # Load the list of repositories
    try:
        with open(REPO, 'rb') as f:
            repos = pickle.load(f)
            repos_ = repos.copy()
            del repos[repo_name]
            f = open(REPO, 'wb')
            pickle.dump(repos, f)
            f.close()
            # Remove apps installed from the deleted repo as listed in INSTALLED
            f = open(INSTALLED, 'rb')
            installed = pickle.load(f)
            f.close()
            apps = []
            for app in installed.keys():
                if installed[app] == repos_[repo_name]:
                    apps.append(app)
                    del installed[app]
            f = open(INSTALLED, 'wb')
            pickle.dump(installed, f)
            f.close()
            
            # Remove apps installed from the deleted repo as listed in APPINFO
            _ = remove_app.remove_list(apps)
            if _["Status"] != "Success":
                return {"Status": "Error", "Detail": _["Detail"]}

    except FileNotFoundError:
        return {'Status': 'error', 'Detail': 'No repositories file found.'} 
    
    return {'Status': 'success', 'Detail': 'Repository removed.'}
