"""
Django Development settings for {{ project_name }}
    * Debug is True
    * Any allowed hosts

This fill will be automatically used when using `manage.py`.
See `base.py` for basic settings.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/

! django-environ uses a confusing NOTYPE, so we are ignoring all env. call type-hints here
"""


from .base import *  # noqa: F403 NOSONAR

# ignore linting errors for undefined names (e.g. env after base * import)
# ruff: noqa: F405

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)  # type: ignore[no-untyped-call]
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    dotenvpath = ROOT_DIR / "envs" / "develop.env"
    if not dotenvpath.exists():
        raise ValueError("Develop dotenv file does not exist (create envs/develop.env)")
    env.read_env(str(dotenvpath), override=True)

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", True)  # type: ignore[no-untyped-call]  # ! in development only!

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="{{ secret_key }}")  # type: ignore[no-untyped-call]

# =====PROJECT-SPECIFIC-SETTINGS===============================================
# add project specific production settings here
PROJECT_FQDN = env.url("PROJECT_FQDN")
# Production checklist:
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
# =============================================================================


# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# for development, we don't need password validation
AUTH_PASSWORD_VALIDATORS = []

# Cors-headers are allowed for development
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",  # Vue Vite
]
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    # de-actived methods:
    # 'DELETE',
    # 'OPTIONS',
    # 'PATCH',
    # 'PUT',
]

CACHES["jwt-blacklist"]["BACKEND"] = "django.core.cache.backends.locmem.LocMemCache"

# The logging-filter 'log_database_queries' will log to the file, if LOG_DATABASE is True
# Turn it only on in develop
LOG_DATABASE = False

# Django Admin URL.
ADMIN_URL = env.str("DJANGO_ADMIN_URL", default="admin/")  # type: ignore[no-untyped-call]

# for development emails are send to console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# alternatively, deactivate email-verification with ACCOUNT_EMAIL_VERIFICATION = 'none'

IPYTHON_ARGUMENTS = ["--debug", "--settings=config.settings.develop"]
# fmt: off
NOTEBOOK_ARGUMENTS = [  # to run the notebook with django 3 async set env DJANGO_ALLOW_ASYNC_UNSAFE=true
    "--port", "8888",
    "--ip", "0.0.0.0",
    "--allow-root",
    "--notebook-dir", "notebooks",
    "--no-browser",
    "--pythonpath", str(ROOT_DIR.resolve()),
]
# fmt: on


# django-extensions------------------------------------------------------------
# debug-toolbar
def show_toolbar(request):
    return False  # True


if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE.insert(4, "debug_toolbar.middleware.DebugToolbarMiddleware")
    # trick to have debug toolbar when developing with docker
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }
