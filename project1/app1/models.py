
from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50, primary_key = True)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    addresDetails=models.CharField(max_length=50)
    hno=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    workExperience=models.CharField(max_length=50)
    companyName=models.CharField(max_length=50)
    fromDate=models.CharField(max_length=50)
    toDate=models.CharField(max_length=50)
    qualificationName=models.CharField(max_length=50)
    percentage=models.CharField(max_length=50)
    project=models.CharField(max_length=50)
    
    
