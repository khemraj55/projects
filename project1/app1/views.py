from functools import partial
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class EmployeeViewSets(viewsets.ViewSet):

    def create(self,request):

        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data={"message":"Faild"}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        queryset=Employee.objects.all()
        serializer=EmployeeSerializer(queryset,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset, pk=pk)
        serializer=EmployeeSerializer(employee)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request,pk=None):

        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset, pk=pk)
        serializer=EmployeeSerializer(data=request.data, instance=employee)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def partial_update(self,request, pk=None):

        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset, pk=pk)
        serializer=EmployeeSerializer(data=request.data, instance=employee, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(sef, request, pk=None):
        queryset=Employee.objects.all()
        employee=get_object_or_404(queryset, pk=pk)
        employee.delete()

        return Response(data={"message":"NO Content"}, status=status.HTTP_204_NO_CONTENT)

class EmployeeModelViewSet(viewsets.ModelViewSet):

    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer





