from django.conf import settings
import environ

def run():
    """things that should run on django startup"""
    env = environ.Env()
    DJANGO_LOADED = env.bool("DJANGO_LOADED", default=False)

    if settings.DEBUG and DJANGO_LOADED:
        # things that should run on django development server startup once(!)
        pass
