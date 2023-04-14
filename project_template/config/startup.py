import environ

from django.conf import settings


def run():
    """things that should run on django startup"""
    env = environ.Env()
    DJANGO_LOADED = env.bool("DJANGO_LOADED", default=False)  # type: ignore[no-untyped-call]

    if settings.DEBUG and DJANGO_LOADED:
        # things that should run on django development server startup once(!)
        pass
