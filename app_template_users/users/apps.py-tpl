from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "apps.users"
    verbose_name = _("Users")

    def ready(self):
        # import here to avoid circular imports
        # try:
        #     from . import signals  # noqa F401
        # except ImportError:
        #     pass
        ...
