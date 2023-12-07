# How to start developing

> Zero to productive..

0. Add the [environment secrets](./environment-secrets.md).

1. Install pyenv & project's python

    Install pyenv for [windows](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md) or [linux/mac](https://github.com/pyenv/pyenv#installation)
    Ensure it's on PATH.

        pyenv install <latest>
        pyenv global <latest>


2. Install poetry

    python -m pip install pipx
    python -m pipx install poetry
    # will add %USERPROFILE%\.local\bin to PATH - be careful, you might want to control your PATH yourself though
    python -m pipx ensurepath  


3. Install projects' python

    # <version>: see pyproject.toml[tool.poetry.dependencies.python]
    pyenv install <version>
    pyenv local <version>  # sets .python-version


4. Install project dependencies

    poetry env use python  # will create the venv and use your current local python
    poetry config virtualenvs.path <global path to your venvs>  # optional
    poetry install  # will install the dependencies to the venv

    # mypy will be used by the project linter, so I recommend to install it globally for a available dmypy on PATH
    # otherwise you will have to configure your IDE and dmypy yourself
    python -m pip install mypy

5. Setup the project for development

    poetry run python commands.py setup
    poetry run python manage.py migrate


6. Install pre-commit hooks

    poetry run pre-commit install  # repeat everytime you re-create the venv


7. Run the devserver

    poetry run python manage.py runserver


8. Run the tests

    poetry run pytest


9. Create devuser

    poetry run python manage.py shell

    $ from django.contrib.auth import get_user_model
    $ email = "test@example.com"
    $ User = get_user_model()
    $ user = User.objects.create(username=email, email=email, is_active=True)
    $ user.set_password("test")
    $ user.save()


10. Handling large files (> 100 MB)

Files larger 10MB will usally trigger the pre-commit-hooks `- id: check-added-large-files\n   args: ['--maxkb=10000']`, 
it is heavily recommended to use [git-lfs](https://git-lfs.com/) for any larger files.
_LFS stores binary files in a separate file system. When you clone a repository,_
_you only download the latest copies of the binary files and not every single_
_changed version of them._

To use LFS you need to install it seperately.  
POSIX: come on, you know how to install software. ;-P  
Windows: Use scoop (https://scoop.sh/) to install git-lfs:.  

```powershell
scoop install main/git-lfs
```

In `.gitattributes` you can define which files should be tracked by lfs.  
Add the files to track (e.g. `*.zip filter=lfs diff=lfs merge=lfs -text`).  

Finally add the lfs hook to the project.

    git lfs install
