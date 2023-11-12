import environs

from django.conf import settings


def run():
    """things that should run on django startup"""
    env = environs.Env()
    DJANGO_LOADED = env.bool("DJANGO_LOADED", default=False)  # pylint: disable=invalid-name

    if settings.DEBUG and DJANGO_LOADED:
        # things that should run on django development server startup once(!)
        pass
