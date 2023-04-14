from typing import Any

from faker import Factory as FakerFactory

from django.conf import settings
from django.contrib.auth import get_user_model

from core.typehints import User, AdminUser


# for all providers see: https://faker.readthedocs.io/en/master/providers.html
# typehinting for faker is not available yet, so we have to use Any
faker: Any = FakerFactory.create()
# ! Faker will have a seed in test mode
faker.seed(settings.TEST_FAKER_SEED)  # type: ignore[misc]


def generic_user_factory(
        first_name: str = "",
        last_name: str = "",
        username: str = "",
        email: str = "",
        password: str = "",
        is_staff: bool = False,
        is_active: bool = False,
        ) -> User:
    """
    User factory.
    Produces a generic the user fixture
    """
    first_name = first_name if first_name else faker.first_name()
    last_name = last_name if last_name else faker.last_name()
    password = password if password else faker.password(length=36, special_chars=True, digits=True, upper_case=True, lower_case=True)
    username = username if username else f"{last_name.lower()}-{first_name.lower()}"
    email = email if email else f"{last_name.lower()}.{first_name.lower()}@{faker.domain_name()}"

    user = get_user_model().objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        is_staff=is_staff,
        is_active=is_active,
    )
    user.set_password(raw_password=password)
    user.save()
    return user


def admin_user_factory(
        first_name: str = "",
        last_name: str = "",
        username: str = "",
        email: str = "",
        password: str = "",
        is_staff: bool = False,
        is_active: bool = False,
        ) -> AdminUser:
    """
    AdminUser factory.
    Produces an adminuser fixture
    """
    user: AdminUser = generic_user_factory(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password,
        is_staff=is_staff,
        is_active=is_active,
    )  # type: ignore[assignment]
    user.is_superuser = True
    user.save()
    return user
