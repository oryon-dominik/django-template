from uuid import uuid4

from django.conf import settings
from django.db import models


class {{ camel_case_app_name }}(models.Model):

    # could be translated: EXCELLENT = 'A', _('Excellent')
    # -> from django.utils.translation import gettext_lazy as _
    class States(models.TextChoices):
        EXCELLENT = 'A', 'Excellent'
        FAILED = 'F', 'Failed'

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    state = models.CharField(
        max_length=1,
        choices=States.choices,
        default=States.EXCELLENT,
    )

    def __str__(self):
        return self.name
