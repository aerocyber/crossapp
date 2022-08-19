"""
    cif_install.py
    ==============

    Install application from crossapp installation file (cif) or install repo from crossapp repo distribution file (crd).
"""


# CIF format
# {
#     "appId": str,
#     "appName": str,
#     "author": str,
#     "version": str,
#     "repo": {
#         "add": bool,
#         "id": str,
#         "name": str,
#         "url": str
#     },
#     "Python": str,
#     "Dependencies": {
#         str: {
#             "PyPi": str,
#             "Version": str
#         },
#     },
#     "pyz": bytes,
#     "EOF": "Reached"
# }

# CRD file format
# {
#     "id": str,
#     "name": str,
#     "url": str
# }


import json
import os
from pathlib import Path


BASE_DIR = os.path.join(Path.home(), ".crossapp")

REPO_DIR = os.path.join(BASE_DIR, "repos")
APPS_DIR = os.path.join(BASE_DIR, "apps")

REPO_DB = os.path.join(REPO_DIR, "repos.json")
APPS_DB = os.path.join(APPS_DIR, "apps.json")

def install_cif(cif_path: str) -> None:
    """Install crossapp based application (cba) from crossapp installation file (cif).

    Args:
        cif_path (str): Path to crossapp installation file.
    """
    ...

def install_crd(crd_path: str) -> None:
    """Install crossapp based application (cba) repository from crossapp distribution file (crd).

    Args:
        crd_path (str): Path to crossapp distribution file.
    """
    ...