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



# Add repo to repo list of repos

import os, pickle

HOME = os.path.expanduser("~")
REPOS = os.path.join(HOME, ".crossapp", "repos.list")

def add(repoName, repoUrl):
    f = open(REPOS, 'rb')
    db = pickle.load(f)
    f.close()
    if (repoName in db.keys()) or (repoUrl in db.values()):
        return {"Status": "Fail", "Detail": "Repo name or Url Exist"}
    
    # Open REPOS file and add repo
    f = open(REPOS, 'wb')
    db[repoName] = repoUrl
    pickle.dump(db, f)
    f.close()
    return {"Status": "Success", "Detail": "Repo added"}


def remove(repoName):
    f = open(REPOS, 'rb')
    db = pickle.load(f)
    f.close()
    if repoName not in db.keys():
        return {"Status": "Fail", "Detail": "Repo name not found"}
    
    # Open REPOS file and remove repo
    f = open(REPOS, 'wb')
    del db[repoName]
    pickle.dump(db, f)
    f.close()
    return {"Status": "Success", "Detail": "Repo removed"}


def update(repoName, repoUrl):
    f = open(REPOS, 'rb')
    db = pickle.load(f)
    f.close()
    if repoName not in db.keys():
        return {"Status": "Fail", "Detail": "Repo name not found"}
    if repoUrl in db.values():
        return {"Status": "Fail", "Detail": "Repo Url Exist"}
    # Open REPOS file and update repo
    f = open(REPOS, 'wb')
    db[repoName] = repoUrl
    pickle.dump(db, f)
    f.close()
    return {"Status": "Success", "Detail": "Repo updated"}

def listRepos():
    f = open(REPOS, 'rb')
    db = pickle.load(f)
    f.close()
    return {"Status": "Success", "Detail": db}
