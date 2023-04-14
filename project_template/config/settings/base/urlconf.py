# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# -----------------------------------------------------------------------------
from . import _secrets
from ._environ import env


# Django Admin URL.
# a little protection to script-kiddie-attacks. This is no REAL security.
ADMIN_URL = _secrets.ADMIN_URL

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "api:api-root"  # "users:redirect"
LOGOUT_REDIRECT_URL = "api:api-root"  # "users:login"
# LOGIN_REDIRECT_URL = "/"
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#login-url
LOGIN_URL = "api:api-root"  # "users:login"

ROOT_URLCONF = 'config.urls.routes'
API_BASE_URL: str = env.str("API_BASE_URL", default="api")  # type: ignore[no-untyped-call]
