# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse

from django.conf import settings
from django.urls import (  # include,
    path,
)
from django.views.generic import RedirectView


app_name = 'api'

# Configure the api root view here
# @api_view(['GET'])
# def api_root(request, format=None):
#     """General project routes available on the api root."""
#     return Response({
#         # 'me': reverse('api:users-user-me', request=request, format=format),
#     })

urlpatterns = [
    # default apis, should not be removed
    # path('', api_root),

    # JWT-authentication
    # path('', include('apps.authentication.api.urls')),

    # this is a fix for the namespace 'api:api-root', that got polluted
    # by the custom apps and has to go last
    path('', RedirectView.as_view(url=''), name='api-root'),
]

if settings.DEBUG:
    # development only
    pass
