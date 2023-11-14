from django.http import HttpRequest
from django.utils import timezone


def add_user_now_fields(request: HttpRequest) -> dict:
    fields = {"lastmodified_by": request.user, "last_modified_at": timezone.now(), "created_by": request.user}
    return fields
