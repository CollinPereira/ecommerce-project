from django.shortcuts import render
from .models import Shoes
from django.shortcuts import render,get_object_or_404

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
    
def puma(request):
    shoes=Shoes.objects.filter(brand__iexact="puma")
    return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Puma'})

def details(request,shoe_id):
    shoe=get_object_or_404(Shoes,pk=shoe_id)
    return render(request,'shoes/details.html',{'shoe':shoe})