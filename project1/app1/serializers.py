from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    
    img=serializers.ImageField(required=False)

    class Meta:
        model=Employee
        fields=['name','email','age','gender','hno','street','city','state','workExperience','companyName','fromDate','toDate','qualificationName','project','percentage','img','addresDetails']