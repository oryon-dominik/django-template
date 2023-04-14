from typing import TypeAlias

from jose import jwt, JWTError
from rest_framework import authentication, status
from rest_framework.exceptions import NotAuthenticated

from django.conf import settings
from django.core.cache import caches

from core.crud.users import get_user_by_email, UserModel
from core.cypher import tokens


MSG_AUTHENTICATION_FAILED = "Authentication failed"
MSG_VERIFICATION_FAILED = "Verification failed"
User: TypeAlias = UserModel


class JWTAuthentication(authentication.BaseAuthentication):
    """
    All authentication classes should extend BaseAuthentication.

    This class is used to authenticate a user based on an access token in the
    request cookies.

    make sure to add this to your settings:
    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            'apps.authentication.api.backends.JWTAuthentication'
        ),
    }

    """

    def authenticate(self, request) -> tuple[User, tokens.JWTAccessToken]:
        """
        Authenticate the request and return a two-tuple of (user, None).
        """
        credentials_exception = NotAuthenticated(
            code=status.HTTP_401_UNAUTHORIZED,
            detail=MSG_AUTHENTICATION_FAILED,
        )

        authentication = request.COOKIES.get(tokens.DEFAULT_JWT_TOKEN_COOKIE_KEY)

        if not authentication:
            raise credentials_exception
        if tokens.DEFAULT_JWT_TOKEN_PREFIX.lower() not in authentication.lower():
            raise credentials_exception

        token: tokens.JWTAccessToken = authentication.removeprefix(
            f"{tokens.DEFAULT_JWT_TOKEN_PREFIX} "
        )  # ! note that the space is required
        if caches["jwt-blacklist"].get(
            token[:247]
        ):  # ! note that the token is truncated to 247 characters, because memcached has a limit of 250 characters
            raise credentials_exception
        try:
            payload: dict = jwt.decode(
                token=token, key=settings.SECRET_KEY, algorithms=[tokens.DEFAULT_JWT_TOKEN_ALGORITHM]
            )
        except JWTError:
            raise credentials_exception
        if payload["type"] != "access":
            raise credentials_exception

        user = get_user_by_email(email=payload["sub"])
        try:
            assert user is not None
        except AssertionError:
            raise credentials_exception
        if not user.is_active:
            raise credentials_exception
        return user, token

    def authenticate_header(self, _):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        www_authenticate = tokens.DEFAULT_JWT_TOKEN_PREFIX
        return www_authenticate
