"""
custom system checks
https://docs.djangoproject.com/en/dev/topics/checks/

Message classes available are:
    Debug
    Info
    Warning
    Error
    Critical

More custom checks in the real world
-> checking translations: https://hakibenita.com/automating-the-boring-stuff-in-django-using-the-check-framework)

"""

from django.conf import settings
from django.core import checks as django_core_checks


class Tags(django_core_checks.Tags):
    """
    Extended custom tags for system checks
    """
    email = "email"


W001 = django_core_checks.Warning(
    "Development settings for `EMAIL_BACKEND` are recommended to be set to"
    " `django.core.mail.backends.console.EmailBackend`.",
    id="core.W001",
)


@django_core_checks.register(Tags.email, deploy=False)
def check_email_backend(app_configs, **kwargs):
    """
    Ensure email backend is console backend in development.
    """
    warnings = []
    if settings.EMAIL_BACKEND != "django.core.mail.backends.console.EmailBackend":
        warnings.append(W001)
    return warnings
