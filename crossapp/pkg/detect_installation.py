"""
    detect_installation.py
    ======================

    API used by various parts of crossapp to detect if an app with a particular
    appId is installed or not.
"""

import json
import os
from pathlib import Path


BASE_DIR = os.path.join(Path.home(), ".crossapp")

REPO_DIR = os.path.join(BASE_DIR, "repos")
APPS_DIR = os.path.join(BASE_DIR, "apps")

REPO_DB = os.path.join(REPO_DIR, "repos.json")
APPS_DB = os.path.join(APPS_DIR, "apps.json")

def installed(appId: str) -> bool:
    f = open(APPS_DB, "r")
    _dt = json.load(f)
    f.close()
    for i in _dt.keys():
        if i == appId:
            return True
    
    return False