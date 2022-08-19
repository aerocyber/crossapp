"""
    get_storage.py
    ==============

    API to get the storage location for a particular application.

"""

import json
import os
from pathlib import Path

from ..pkg import detect_installation


BASE_DIR = os.path.join(Path.home(), ".crossapp")

REPO_DIR = os.path.join(BASE_DIR, "repos")
APPS_DIR = os.path.join(BASE_DIR, "apps")

REPO_DB = os.path.join(REPO_DIR, "repos.json")
APPS_DB = os.path.join(APPS_DIR, "apps.json")

# Info
# ====
#
# Apps are stored in APPS_DIR/{appId}/
# Repos are stored in REPO_DIR/{repoId}/
# Record of apps and associated app locations, repos, etc are stored in APPS_DB
# Record of apps installable from a repo, etc are stored in REPO_DB

for i in [BASE_DIR, REPO_DIR, APPS_DIR]:
    if not os.path.exists(i):
        os.mkdir(i)

for i in [REPO_DB, APPS_DB]:
    if not os.path.exists(i):
        f = open(i, "w")
        f.write(json.dumps({}))
        f.close()


class NotInstalledException(Exception):
    pass


def get(appId: str) -> dict:
    """Get the temporary location for app.

    Args:
        appId (str): The appId of the app that requests this data

    Returns:
        dict: The required data of the following spec:
        {
            "appId": appId,
            "temporary location": <str>,
        }
    """
    is_installed = detect_installation.installed(appId)
    if not is_installed:
        raise NotInstalledException(f"{appId} needs to be installed to use APIs provided by crossapp")
    tmp_dir = os.path.join(APPS_DIR, appId, "tmp")
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    
    return {
            "appId": appId,
            "temporary location": tmp_dir,
        }
