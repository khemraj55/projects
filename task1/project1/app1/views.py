from django.shortcuts import render,redirect
from .models import Category,Product
from .forms import CategoryForm, ProductForm

from django.http import HttpResponse

# Create your views here.

def Categoryview(request):
    form =CategoryForm()
    template_name='app1/category.html'

    if request.method=='POST':
        form=CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pro_urls')
    context={'form':form}
    return render(request,template_name,context)

def Productview(request):
    form =ProductForm()
    template_name='app1/product.html'

    if request.method=='POST':
        form =ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_urls')
    context={'form':form}
    return render(request, template_name, context)

def displayview(request):
    c =Category.objects.all()
    p= Product.objects.all()

    template_name='app1/display.html'
    context={'Category':c,'Product':p}


    return render(request,template_name,context)
