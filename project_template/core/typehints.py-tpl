from typing import TypeAlias

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AbstractBaseUserWithPermissions(PermissionsMixin, AbstractBaseUser):  # type: ignore[misc]
    pass


# The user is atleast an AbstractBaseUser
User: TypeAlias = AbstractBaseUser
# The adminuser is atleast an AbstractBaseUserWithPermissions
AdminUser: TypeAlias = AbstractBaseUserWithPermissions
