# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# -----------------------------------------------------------------------------
from . import paths


# DATABASES
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
# Postgres:
# POSTGRES_DB = env.str("POSTGRES_DB", default="{{ project_name }}")
# POSTGRES_USER = env.str("POSTGRES_USER")
# POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
# POSTGRES_HOST = env.str("POSTGRES_HOST")
# POSTGRES_PORT = env.int("POSTGRES_PORT")
# POSTGRES_OPTIONS = ""
# POSTGRES_SSL = "require" if DEBUG else "allow"
# POSTGRES_CONNECTION_STRING = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}{POSTGRES_OPTIONS}"
# DATABASE_URL = env.str("DATABASE_URL", default=POSTGRES_CONNECTION_STRING)
# DATABASES = {"default": env.db("DATABASE_URL", default=DATABASE_URL)}
# SQLite:
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': paths.ROOT_DIR / 'database' / 'sqlite3.db'}}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Default primary key field type
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake-{{ project_name }}-cache',
    },
    'jwt-blacklist': {
        # 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # ! this is not thread-safe and not recommended, if you use multiple workers
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # ! this is slow in production. Maybe use redis or memcached
        'LOCATION': 'blacklisted_jwts_cache',
    }
}
