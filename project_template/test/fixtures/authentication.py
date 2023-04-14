from datetime import timedelta

import pytest
from jose import jwt

from django.conf import settings
from django.utils import timezone

from core.cypher import tokens


@pytest.fixture
def invalid_refresh_token(verified_user):
    # Obtain a new refresh token with an invalid secret key
    now = timezone.now()
    claims = {
        "iss": settings.PROJECT_FQDN,
        "exp": now + timedelta(minutes=tokens.DEFAULT_JWT_TOKEN_REFRESH_EXPIRATION_MINUTES),
        "sub": verified_user.email,
        "iat": now,
        "zoneinfo": settings.TIME_ZONE,
    }
    headers = {
        "alg": tokens.DEFAULT_JWT_TOKEN_ALGORITHM,
        "typ": tokens.DEFAULT_JWT_TOKEN_TYPE,
    }
    return tokens.JWTAccessToken(jwt.encode(claims=claims, key='unknown', algorithm=tokens.DEFAULT_JWT_TOKEN_ALGORITHM, headers=headers))


@pytest.fixture
def valid_refresh_token(verified_user):
    # Obtain a new refresh token with a valid secret key
    now = timezone.now()
    claims = {
        "iss": settings.PROJECT_FQDN,
        "exp": now + timedelta(minutes=tokens.DEFAULT_JWT_TOKEN_REFRESH_EXPIRATION_MINUTES),
        "sub": verified_user.email,
        "iat": now,
        "zoneinfo": settings.TIME_ZONE,
    }
    headers = {
        "alg": tokens.DEFAULT_JWT_TOKEN_ALGORITHM,
        "typ": tokens.DEFAULT_JWT_TOKEN_TYPE,
    }
    return tokens.JWTAccessToken(jwt.encode(claims=claims, key=settings.SECRET_KEY, algorithm=tokens.DEFAULT_JWT_TOKEN_ALGORITHM, headers=headers))
