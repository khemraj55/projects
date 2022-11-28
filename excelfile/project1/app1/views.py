from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer, SignUpSerializers
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]

class SignUpAPI(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=SignUpSerializers

import pandas as pd
from django.conf import settings
import uuid

class ExcelFileAPI(APIView):

    def get(self, request):
        student_obj=Student.objects.all()
        serializer=StudentSerializer(student_obj, many=True)

        df=pd.DataFrame(serializer.data)
        print(df)

        df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv", encoding="UTF-8", index=False)

        return Response({'status':200})

    
