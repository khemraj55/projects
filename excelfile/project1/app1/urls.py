from django.urls import path
from .views import SignUpAPI, ExcelFileAPI


urlpatterns=[
    path('register/',SignUpAPI.as_view(),name='register'),
    path('excel/',ExcelFileAPI.as_view(), name='excel')
]