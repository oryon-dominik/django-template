# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# -----------------------------------------------------------------------------
from . import paths
from . import security


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#logging

# The following loglevels are available:
# - CRITICAL    (50)
# - ERROR       (40)
# - WARNING     (30)
# - INFO        (20)
# - DEBUG       (10)
# - NOTSET      (0)
# The default level shall be WARNING.
# The default level for the console can be INFO.

# The logging-filter 'log_database_queries' will log to the file, if LOG_DATABASE is True
# Turn it only on in develop
LOG_DATABASE = False

# See https://docs.djangoproject.com/en/{{ docs_version }}/topics/logging for
# more details on how to customize your logging configuration.
LOGGING_FILE_HANDLER = "logging.FileHandler"

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "log_database_queries": {
            "()": "config.logfilters.LogDatabaseQueriesFilter",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple" if security.DEBUG else "verbose",
        },
        "requests_file": {
            "level": "INFO",
            "class": LOGGING_FILE_HANDLER,
            "filename": str(paths.ROOT_DIR / "logs" / "requests.log"),
        },
        "database_queries_file": {
            "level": "DEBUG",
            "filters": ["log_database_queries"],
            "class": LOGGING_FILE_HANDLER,
            "filename": str(paths.ROOT_DIR / "logs" / "queries.log"),
        },
        "server_log_file": {
            "level": "INFO",
            "class": LOGGING_FILE_HANDLER,
            "filename": str(paths.ROOT_DIR / "logs" / "server.log"),
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "server_log_file"],
            "level": "INFO",
            "propagate": True,
        },
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["database_queries_file"],
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "server_log_file"],
            "propagate": False,
        },
    },
}
