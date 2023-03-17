from django.urls import path

from . import views


app_name = "{{ app_name }}s"

urlpatterns = [
    path("", views.{{ camel_case_app_name }}Index.as_view(), name="index"),
    path('{{ app_name }}s/', views.{{ camel_case_app_name }}List.as_view(), name='list'),
    path('{{ app_name }}s/<uuid:pk>', views.{{ camel_case_app_name }}Detail.as_view(), name='detail'),
    path('{{ app_name }}s/create/', views.{{ camel_case_app_name }}Create.as_view(), name='create'),
    path('{{ app_name }}s/update/<uuid:pk>', views.{{ camel_case_app_name }}Update.as_view(), name='update'),
    path('{{ app_name }}s/delete/<uuid:pk>', views.{{ camel_case_app_name }}Delete.as_view(), name='delete'),
]
