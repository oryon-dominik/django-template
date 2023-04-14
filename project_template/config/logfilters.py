import logging

from django.conf import settings


class LogDatabaseQueriesFilter(logging.Filter):
    def filter(self, record):
        return settings.LOG_DATABASE
