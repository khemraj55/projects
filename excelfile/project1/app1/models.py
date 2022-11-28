from django.db import models

# Create your models here.

class Student(models.Model):
    rn=models.IntegerField()
    name=models.CharField(max_length=50)


class Excelfile(models.Model):
    excel_file_upload=models.FileField(upload_to='excel')



