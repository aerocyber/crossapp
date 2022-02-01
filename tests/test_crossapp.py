from crossapp import __version__, install, envCreate, repo_
import os
import pickle
import shutil


def test_variables():
    assert __version__ == '1.0.0-alpha.1'
    assert install.HOME_DIR == os.path.expanduser("~")
    assert install.CROSSAPP_DIR == os.path.join(install.HOME_DIR, ".crossapp")
    assert install.VIRTUALENV_DIR == os.path.join(
        install.CROSSAPP_DIR, "virtualenv")
    assert install.DATABASE_DIR == os.path.join(
        install.CROSSAPP_DIR, "database")
    assert install.DATABASE_FILE == os.path.join(
        install.DATABASE_DIR, "crossapp.db")
    assert add_repo.REPO_LIST_FILE == os.path.join(
        install.CROSSAPP_DIR, 'repositories', "repos.db")


def test_functions():
    install.create_crossapp_dir()
    assert os.path.exists(install.CROSSAPP_DIR) == True
    install.create_virtualenv_dir()
    assert os.path.exists(install.VIRTUALENV_DIR) == True
    install.create_database_dir()
    assert os.path.exists(install.DATABASE_DIR) == True
    install.create_database_file()
    assert os.path.exists(install.DATABASE_FILE) == True
    a = envCreate.createEnv(install.VIRTUALENV_DIR)
    a.create_virtual_env()
    assert os.path.exists(os.path.join(install.VIRTUALENV_DIR, "bin")) == True
    b = add_repo.repoManagement('samplerepo', 'test repo')
    b.add_repo()
    assert os.path.exists(add_repo.REPO_LIST_FILE) == True
    assert os.path.exists(os.path.join(
        install.CROSSAPP_DIR, 'repositories')) == True
    f = open(add_repo.REPO_LIST_FILE, 'rb')
    data = pickle.load(f)
    f.close()
    assert data[0]['samplerepo'] == 'test repo'
    c = add_repo.repoManagement('samplerepo1', 'test repo')
    c.update_repo()
    f = open(add_repo.REPO_LIST_FILE, 'rb')
    data = pickle.load(f)
    f.close()
    assert data['samplerepo1'] == 'test repo'
    c.remove_repo()
    f = open(add_repo.REPO_LIST_FILE, 'rb')
    data = pickle.load(f)
    f.close()
    assert data['samplerepo1'] == None


# def test_cleanup():
#     # Clean the directories created.
#     shutil.rmtree(install.VIRTUALENV_DIR)
#     shutil.rmtree(install.DATABASE_DIR)
#     os.remove(add_repo.REPO_LIST_FILE)
#     shutil.rmtree(install.CROSSAPP_DIR)
#     assert os.path.exists(add_repo.REPO_LIST_FILE) == False
#     assert os.path.exists(install.CROSSAPP_DIR) == False
#     assert os.path.exists(install.VIRTUALENV_DIR) == False
#     assert os.path.exists(install.DATABASE_DIR) == False
#     assert os.path.exists(install.DATABASE_FILE) == False
