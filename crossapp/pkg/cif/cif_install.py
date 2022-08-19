"""
    cif_install.py
    ==============

    Install application from crossapp installation file (cif) or install repo from crossapp repo distribution file (crd).
"""

from genericpath import exists
import json
from msilib import schema
from xml.dom import ValidationErr
from jsonschema import validate
import os
from pathlib import Path
from platform import system


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


# CIF format
# ==========
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
# ===============
# {
#     "id": str,
#     "name": str,
#     "url": str
# }


# APPS_DB format
# ==============
# {
#     appId: {
#         "Install Path": str,
#         "Dependencies path": str,
#         "Added repo": bool,
#         "Python path": str
#     }
# }

_py = 'python'
if (system().lower() == "windows") or (system().lower() == "nt"):
    _py = "python.exe"


def validate_cif(cif_file_content: dict) -> None:
    """Validate the cif file content

    Args:
        cif_file_content (dict): The content of cif file.
    """
    try:
        schema = {
            "type": "object",
            "properties": {"appId": {"type": "string"},
                           "appName": {"type": "string"},
                           "author": {"type": "string"},
                           "version": {"type": "string"},
                           "repo": {
                               "add": {"type": "bool"},
                               "id": {"type": "string"},
                               "name": {"type": "string"},
                               "url": {"type": "string"}
            },
                "Python": {"type": "string"},
                "Dependencies": {
                               {"type": "string"}: {
                                   "PyPi": {"type": "string"},
                                   "Version": {"type": "string"}
                               },
            },
                "pyz": bytes,
            },
        }
        validate(instance=cif_file_content, schema=schema)
    except ValidationError:
        raise ValidationError("Invalid cif file")
    else:
        if cif_file_content["EOF"] != "Reached":
            raise ValidationError("Invalid cif file")


def validate_crd(crd_file_content: dict) -> None:
    try:
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "url": {"type": "string"}
            }
        }
        validate(instance=crd_file_content, schema=schema)
    except ValidationError:
        raise ValidationError("Invalid repo")
    else:
        if cif_file_content["EOF"] != "Reached":
            raise ValidationError("Invalid repo")


def install_cif(cif_path: str) -> None:
    """Install crossapp based application (cba) from crossapp installation file (cif).

    Args:
        cif_path (str): Path to crossapp installation file.
    """
    if not os.path.exists(cif_path):
        raise FileNotFoundError(f"{cif_path} was not found.")

    f = open(cif_path, "r")
    _cif = json.load(f)
    f.close()
    validate_cif(_cif)

    if not os.path.exists(os.path.join(APPS_DIR, _cif["appId"])):
        os.mkdir(os.path.join(APPS_DIR, _cif["appId"]))

    if not os.path.exists(os.path.join(APPS_DIR, _cif["appId"], "dependencies")):
        os.mkdir(os.path.join(APPS_DIR, _cif["appId"], "dependencies"))

    if not os.path.exists(os.path.join(BASE_DIR, "python")):
        os.mkdir(os.path.join(BASE_DIR, "python"))

    if not os.path.exists(os.path.join(BASE_DIR, "python", _cif["Python"])):
        os.mkdir(os.path.join(BASE_DIR, "python", _cif["Python"]))

    _f = open(os.path.join(
        APPS_DIR, _cif["appId"], _cif["name"]) + ".pyz", 'w')
    _f.write(_cif["pyz"])
    _f.close()

    if _cif["repo"]["add"]:
        repo_ = open(REPO_DB, 'r')
        repos = json.load(repo_)
        repo_.close()
        _r = _cif["repo"]
        del _r["id"]
        validate_crd(_r)
        repos[_cif["repo"][id]]

    f = open(APPS_DB, 'r')
    dt = json.load(f)
    f.close()

    dt[_cif["appId"]] = {
        "Install Path": str(os.path.join(APPS_DIR, _cif["appId"], _cif["name"]) + ".pyz"),
        "Dependencies path": str(os.path.join(APPS_DIR, _cif["appId"], "dependencies")),
        "Added repo": _cif["repo"]["add"],
        "Python path": str(os.path.join(BASE_DIR, "python", _cif["Python"], _py))
    }


def install_crd(crd_path: str) -> None:
    """Install crossapp based application (cba) repository from crossapp distribution file (crd).

    Args:
        crd_path (str): Path to crossapp distribution file.
    """
    pass
