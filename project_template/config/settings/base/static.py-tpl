# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# -----------------------------------------------------------------------------
from . import paths


# STATIC files (CSS, JavaScript, Images)
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_ROOT = str(paths.ROOT_DIR / "staticfiles")
# To use a CDN (e.g.: for whitenoise), SET a statichost, (preferably as env):
STATIC_HOST = ""
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = f"{STATIC_HOST}/assets/"
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(paths.ROOT_DIR / "assets")]
# See: https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "config.finders.AssetsAppDirectoriesFinder",
]
MEDIA_ROOT = str(paths.ROOT_DIR / "media")
MEDIA_URL = f"{STATIC_HOST}/media/"
