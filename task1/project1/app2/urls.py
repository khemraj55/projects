from django.urls import path
from .views import SignUpAPI


urlpatterns=[
    path('register/',SignUpAPI.as_view(), name='register'),
]