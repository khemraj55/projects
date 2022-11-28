from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['c_id','mobile','laptop']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_id','year','brand','model_name','combine']
admin.site.register(Product, ProductAdmin)