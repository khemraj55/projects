from django.urls import path
from .import views

urlpatterns=[
    path('cv/',views.Categoryview,name='cat_urls'),
    path('pv/',views.Productview, name='pro_urls'),
    path('dv/',views.displayview, name='display_urls')
]