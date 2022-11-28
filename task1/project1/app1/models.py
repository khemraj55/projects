from django.db import models

class Category(models.Model):
    c_id = models.IntegerField(primary_key=True)
    mobile = models.CharField(max_length=50)
    laptop = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.c_id}--{self.mobile}--{self.laptop}'

class Product(models.Model):
    category =models.ManyToManyField(Category)
    p_id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    brand = models.CharField(max_length=50)
    model_name=models.CharField(max_length=50)


    def combine(self):
        return " , ".join([str(p) for p in self.category.all()])