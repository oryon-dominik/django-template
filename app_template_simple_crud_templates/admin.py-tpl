from collections.abc import Iterable
from typing import TypeAlias

from django.conf import settings
from django.contrib import admin
from django.db.models import Model
from django.db.models.base import ModelBase

from . import models


ModelType: TypeAlias = type[Model] | Iterable[type[Model]]

# register all models when debugging
if settings.DEBUG:
    for model_name in dir(models):
        model: ModelType = getattr(models, model_name)

        if (
            isinstance(model, ModelBase)
            and model_name != "Model"
            and hasattr(model, "_meta")
            and hasattr(model._meta, "abstract")  # type: ignore
            and not model._meta.abstract  # type: ignore
        ):
            admin.site.register(model)
