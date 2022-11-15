from django.urls import path
from .views import EmployeeModelViewSet

urlpatterns=[
    path('employee/',EmployeeModelViewSet.as_view({'post':'create','get':'list'}),name='emp'),
    path('employee/<int:pk>/',EmployeeModelViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='employee-update')

]