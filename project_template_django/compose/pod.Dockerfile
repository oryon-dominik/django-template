# TODO: setup this application as it's own deployable pod - or something similar

FROM python:3.11-slim


RUN apt-get update \
    && apt install --assume-yes --no-install-recommends \
    # gcc
    curl


ENV \
    # -- python ENVS
    # Python will intercept errors and dump a stack trace (faulthandler.enable() on startup)
    # https://docs.python.org/3/using/cmdline.html?highlight=pythonfaulthandler#envvar-PYTHONFAULTHANDLER
    PYTHONFAULTHANDLER=1 \
    # Keeps Python from generating .pyc files in the container
    PYTHONDONTWRITEBYTECODE=1 \
    # Turns off buffering for easier container logging
    PYTHONUNBUFFERED=1 \
    # venv path
    VENV_PATH="/opt/python/venvs" \
    # -- pip ENVS
    # https://pip.pypa.io/en/stable/topics/configuration/#environment-variables
    # Disable the cache.
    PIP_NO_CACHE_DIR=1 \
    # Raise the default timeout to 100 seconds.
    PIP_DEFAULT_TIMEOUT=100 \
    # -- poetry ENVS
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    # Poetry home directory will live in `/opt`.
    POETRY_HOME="/opt/python/poetry" \
    POETRY_CACHE="/opt/python/cache" \
    # Create virtual environment in the project's root `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # Do not create virtual environment if it does not exist
    POETRY_VIRTUALENVS_CREATE=false \
    # Do not ask any interactive question
    POETRY_NO_INTERACTION=1

ENV \
    # Prepend poetry / venv bins to path (needs POETRY_HOME and VENV_PATH to be set)
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN echo "export PATH=${PATH}" >> /root/.bashrc


RUN python -m pip install --upgrade pip \
    && curl -sSL https://install.python-poetry.org | python -

COPY ./entrypoint.sh /app

WORKDIR /app

# Install all non optional dependency-groups
RUN poetry install --sync

# TBD: create a special user for the app?
# RUN adduser --disabled-password --gecos '' app
# USER app
# TBD: chown the appdir?

# Run entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]
