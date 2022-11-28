from django.db import models

class Employee(models.Model):
    eid=models.IntegerField()
    salary=models.FloatField()
    

    
