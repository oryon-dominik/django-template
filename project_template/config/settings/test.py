"""
Django settings for {{ project_name }} project in test mode

Make sure to override `DJANGO_SETTINGS_MODULE` environment variable to use this file.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""
from corsheaders.defaults import default_methods

from .base import *  # noqa: F403 NOSONAR

# ignore linting errors for undefined names (e.g. env after base * import)
# ruff: noqa: F405

# Read environment from .env
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)  # type: ignore[no-untyped-call]
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    dotenvpath = ROOT_DIR / "envs" / "test.env"
    if not dotenvpath.exists():
        raise ValueError("Test dotenv file does not exist (create envs/test.env)")
    env.read_env(str(dotenvpath), override=True)

SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="{{ secret_key }}")  # type: ignore[no-untyped-call]

# =====PROJECT-SPECIFIC-SETTINGS===============================================
# add project specific production settings here
PROJECT_FQDN = env.url("PROJECT_FQDN", default="http://localhost:8000")  # type: ignore[no-untyped-call]
# Production checklist:
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
# =============================================================================


# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#test-runner
IS_TESTING = True

ALLOWED_HOSTS = ["testserver"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = list(default_methods)

INSTALLED_APPS += []

CACHES["jwt-blacklist"]["BACKEND"] = "django.core.cache.backends.locmem.LocMemCache"

TEST_RUNNER = "test.runners.PytestTestRunner"
TEST_FAKER_SEED = 1337

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#email-port
EMAIL_PORT = 1025

# Make tests faster by using a noop hasher
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

LOGGING["loggers"]["django.db.backends"]["level"] = "INFO"
