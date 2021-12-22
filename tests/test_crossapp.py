from crossapp import __version__, install, envCreate
import os
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


def test_cleanup():
    # Clean the directories created.
    shutil.rmtree(install.VIRTUALENV_DIR)
    shutil.rmtree(install.DATABASE_DIR)
    shutil.rmtree(install.CROSSAPP_DIR)
    assert os.path.exists(install.CROSSAPP_DIR) == False
    assert os.path.exists(install.VIRTUALENV_DIR) == False
    assert os.path.exists(install.DATABASE_DIR) == False
    assert os.path.exists(install.DATABASE_FILE) == False
