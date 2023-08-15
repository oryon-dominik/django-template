from typing import TypeAlias

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AbstractBaseUserWithPermissionsType(PermissionsMixin, AbstractBaseUser):  # type: ignore[misc]
    """
    The adminuser is atleast an AbstractBaseUserWithPermissions
    - has an email field
    - and neccessary permissions.
    """

    ...

    class Meta:
        abstract = True


UserType: TypeAlias = AbstractBaseUser
AdminUserType: TypeAlias = AbstractBaseUserWithPermissionsType
