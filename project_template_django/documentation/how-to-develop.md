# How to start developing

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

3. install projects python

        # <version>: see pyproject.toml[tool.poetry.dependencies.python]
        pyenv install <version>
        pyenv local <version>  # sets .python-version

4. Install project dependencies

        poetry config virtualenvs.path <global path to your venvs>  # optional
        poetry install  # will create the venv

5. Install pre-commit hooks

        poetry run pre-commit install
