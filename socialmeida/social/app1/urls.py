from django.urls import path
from .views import post_detailview

urlpatterns=[
    path('co/',post_detailview)
]