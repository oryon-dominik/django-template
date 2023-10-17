#!/usr/bin/env python
import os

import celery

from django.conf import settings


# for handling redis with certificates: import ssl


# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

app = celery.Celery(
    "tasks",
    broker=settings.REDIS_URL,  # type: ignore[misc]
    backend=settings.REDIS_URL,  # type: ignore[misc]
    broker_use_ssl={
        # 'ssl_keyfile': settings.REDIS_KEY_FILE, 'ssl_certfile': settings.REDIS_CERT_FILE,
        # 'ssl_ca_certs': settings.REDIS_CA_FILE,
        # 'ssl_cert_reqs': ssl.CERT_NONE
    },
    redis_backend_use_ssl={
        # 'ssl_keyfile': settings.REDIS_KEY_FILE, 'ssl_certfile': settings.REDIS_CERT_FILE,
        # 'ssl_ca_certs': settings.REDIS_CA_FILE,
        # 'ssl_cert_reqs': ssl.CERT_NONE
    },
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# --- examples ----------------------------------------------------------------

# example tasks.py
# from config.celeryapp import app
# @app.task(bind=True, name="debug.debugging-task")
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# examples for task types
# import logging
# celery_fail_logger = logging.getLogger('celery-failed-tasks')
# EXCEPTIONS: tuple = ()  # (RuntimeError, HTTPError)
# MAX_RETRIES = 10
# class LoggingTask(celery.Task):
#     def on_failure(self, exc, task_id, args, kwargs, einfo):
#         celery_fail_logger.exception('Task failed: %s' % exc, exc_info=exc)
#         super().on_failure(exc, task_id, args, kwargs, einfo)
# class RetryingTask(celery.Task):
#     autoretry_for = EXCEPTIONS
#     retry_kwargs = {'max_retries': MAX_RETRIES}
#     retry_backoff = True
#     retry_backoff_max = 60 * 60 * 1  # 1 hour
#     retry_jitter = True  # randomness in backoff delay

# class LoggingAndRetryingTask(RetryingTask, LoggingTask):
#     pass
