from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer, SignUpSerializer
from .models import Employee
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class SignUpAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer