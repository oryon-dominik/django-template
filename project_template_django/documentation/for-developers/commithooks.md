# commit hooks

TODO: reactivate pyupgrade after the support for typing.Optional is added in 1.0 of typer

[Pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks) are defined
in `.pre-commit-config.yaml`. Adding them to the project will ensure that the
code is formatted and linted before committing. Repeat the installation
everytime you re-create the venv  

    poetry run pre-commit install


## used hooks

(see documentation in the respective repositories and more configuration options in `.pre-commit-config.yaml`)

- https://github.com/pre-commit/pre-commit-hooks  
    trailing-whitespace --markdown-linebreak-ext=md  
    end-of-file-fixer  
    check-yaml  
    check-added-large-files --maxkb=10000  

- https://github.com/adamchainz/django-upgrade  
    django-upgrade --target-version, "4.1"  

- https://github.com/psf/black  
    black --force-exclude='pyproject.toml'  

- https://github.com/charliermarsh/ruff-pre-commit  
    ruff  

- https://github.com/timothycrosley/isort  
    isort  

- https://github.com/PyCQA/flake8  
    flake8  

- https://github.com/rtts/djhtml  
    djhtml --tabwidth, "2"  

- https://github.com/pre-commit/mirrors-mypy  
    mypy --no-warn-unused-ignores, --ignore-missing-imports  

