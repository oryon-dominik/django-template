from django.conf import settings
from django.urls import path

from . import views


urlpatterns = [
    path('auth/token/', views.AuthTokenLogin.as_view(), name='login'),
    path('auth/token/verify/', views.AuthTokenVerify.as_view(), name='verify'),
    path('auth/token/refresh/', views.AuthTokenRefresh.as_view(), name='refresh'),
    path('auth/token/logout/', views.AuthTokenLogout.as_view(), name='logout'),
]

if hasattr(settings, 'IS_TESTING'):
    
    """
    EXAMPLE PROTECTED VIEW below
    """

    from rest_framework.permissions import IsAuthenticated, BasePermission
    from rest_framework.views import APIView

    from django.http import JsonResponse

    from .backends import JWTAuthentication

    class CustomAdminPermission(BasePermission):
        """Return `True` if permission is granted, `False` otherwise."""
        def has_permission(self, request, view): return request.user.is_superuser
        def has_object_permission(self, request, view, obj): return True

    class ProtectionTestView(APIView):
        """
        ... example view that requires authentication.

        * Requires token authentication.
        """
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]  # default permission is "is authenticated"

        def get(self, request, format=None):
            """
            Return a list of all users.
            """
            foo = ['foo', 'bar', 'baz']
            return JsonResponse({'foo': foo})

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
            Return a list of all users.
            """
            foo = ['foo', 'bar', 'baz']
            return JsonResponse({'foo': foo})


    urlpatterns += [
        path('protectiontest/', ProtectionTestView.as_view(), name='test-protected'),
        path('adminprotectiontest/', AdminProtectionTestView.as_view(), name='test-protected'),
    ]
