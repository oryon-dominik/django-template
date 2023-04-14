from django.urls import include, path

from . import views
from .routers import {{ app_name }}_router


app_name = "{{ app_name }}"

urlpatterns = [
    path('', include({{ app_name }}_router.urls)),
]
