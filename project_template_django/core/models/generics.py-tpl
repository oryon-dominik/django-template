import uuid

from django.conf import settings
from django.db import models


class UUIDModel(models.Model):
    """Generate a uuid 4 as primary key.

    A uuid could be duplicated, this may cause a UniqueViolationError and fail, if that uuid already exists..
    although that is extremely unlikely: to have a 50% chance of a duplicate, you need (~ 2.71 * 10**18) generations
    => the chance to have a duplicate in ~ 100_000_000_000_000 uuids is roughly 1:1_000_000_000
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # type: ignore[var-annotated]

    class Meta:
        abstract = True


class IndexedTimeStampedModel(models.Model):
    """TimeStampedModel

    An abstract base class model that provides self-managed "created_at" and
    "lastmodified_at" fields. DB-indexed.
    """

    created_at = models.DateTimeField("Created at", auto_now_add=True, db_index=True)
    lastmodified_at = models.DateTimeField("Last modified at", auto_now=True, db_index=True)

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """
    UserInfoModel

    An abstract base class model that provides self-managed "created_by" and
    "lastmodified_by" fields.
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Created by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
    )
    lastmodified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Last modified by",
        blank=True,
        null=True,
        related_name="%(app_label)s_%(class)s_lastmodified",
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_by = kwargs.pop("created_by", None)
        else:
            # We won't allow to change the created_by field if the model had been saved already.
            kwargs.pop("created_by", None)
        self.lastmodified_by = kwargs.pop("lastmodified_by", None)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class StampedUUIDModel(UUIDModel, IndexedTimeStampedModel, UserStampedModel):
    """
    StampedUUIDModel

    provides auto TimeStamps, UserInfo and UUID-pks
    """

    class Meta:
        abstract = True
