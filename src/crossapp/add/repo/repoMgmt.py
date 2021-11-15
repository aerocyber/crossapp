# Add repo to repo list of repos

import os, pickle

HOME = os.path.expanduser("~")
REPOS = os.path.join(HOME, "crossapp", "repos.list")

def add(repoName, repoUrl):
    f = open(REPOS, 'rb')
    db = pickle.load(f)
    f.close()
    if (repoName in db.keys()) or (repoUrl in db.values()):
        return {"Status": "Fail", "Detail": "Repo name or Url Exist"}
    
    