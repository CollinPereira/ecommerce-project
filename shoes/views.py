from django.shortcuts import render
from .models import Shoes
# Create your views here.
def home(request):
    shoes=Shoes.objects.all().order_by('-date')[:9]
    return render(request,'shoes/home.html',{'shoes':shoes})

def nike(request):
    shoes=Shoes.objects.filter(brand__iexact="nike")
    return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Nike'})

def adidas(request):
    shoes=Shoes.objects.filter(brand__iexact="adidas")
    return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Adidas'})

def details(request):
    return render(request,'shoes/details.html',{})