from django.conf import settings
from django.urls import path

from . import views


urlpatterns = [
    path(route="auth/token/", view=views.AuthTokenLogin.as_view(), name="login"),  # type: ignore
    path(route="auth/token/verify/", view=views.AuthTokenVerify.as_view(), name="verify"),  # type: ignore
    path(route="auth/token/refresh/", view=views.AuthTokenRefresh.as_view(), name="refresh"),  # type: ignore
    path(route="auth/token/logout/", view=views.AuthTokenLogout.as_view(), name="logout"),  # type: ignore
]

if hasattr(settings, "DJANGO_RUNS_IN_TESTMODE"):
    """
    EXAMPLE PROTECTED VIEW below
    """

    from rest_framework.permissions import IsAuthenticated, BasePermission
    from rest_framework.views import APIView

    from django.http import JsonResponse

    from .backends import JWTAuthentication

    class CustomAdminPermission(BasePermission):
        """Return `True` if permission is granted, `False` otherwise."""

        def has_permission(self, request, view):
            """
            ! request.user might not have is_superuser attribute outside of testing
            """
            return request.user.is_superuser  # type: ignore

        def has_object_permission(self, request, view, obj):
            return True

    class ProtectionTestView(APIView):
        """
        ... example view that requires authentication.

        * Requires token authentication.
        """

        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]  # default permission is "is authenticated"

        def get(self, request, format=None):
            """
            Return a list of all planets.
            """
            planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
            return JsonResponse({"planets": planets})

    class AdminProtectionTestView(APIView):
        """
        ... example view that requires authentication.

        * Requires token authentication.
        * Only admin users are able to access this view.
        """

        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated, CustomAdminPermission]  # default permission is "is authenticated"

        def get(self, request, format=None):
            """
            Return a list of all planets.
            """
            planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
            return JsonResponse({"planets": planets})

    urlpatterns += [
        path("protectiontest/", ProtectionTestView.as_view(), name="test-protected"),  # type: ignore
        path("adminprotectiontest/", AdminProtectionTestView.as_view(), name="test-protected"),  # type: ignore
    ]
