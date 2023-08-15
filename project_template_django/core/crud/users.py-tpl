from django.contrib.auth import get_user_model

from ..typehints.django import UserType


UserModel = get_user_model()


def get_user_by_email(email: str) -> UserType | None:
    try:
        return UserModel.objects.get(email=email)
    except UserModel.DoesNotExist:
        return None
