"""Will get imported via __init__.py on module level"""
import secrets

from functools import lru_cache

from . import logs


@lru_cache()
def get_settings():
    """
    Get settings from config.
    @Least-recently-used cache decorator.
    -> Return the same value that was returned the first time, instead of computing it again.
    """
    return Settings(**{})


class Settings:
    """
    Settings for the application.

    Use Typehints to ensure your IDE will moan, if the types get messed up.
    """

    # -> https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # logging
    LOG_LEVEL = logs.LOG_LEVEL
