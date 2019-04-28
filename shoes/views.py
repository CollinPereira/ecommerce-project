from django.shortcuts import render
from .models import Shoes
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.db.models import Q 

# Create your views here.
def home(request):
    shoes=Shoes.objects.all().order_by('-date')[:9]
    return render(request,'shoes/home.html',{'shoes':shoes})


class NikeListView(ListView):
    model=Shoes
    queryset = Shoes.objects.filter(brand__iexact="nike")
    template_name = 'shoes/brand.html'
    context_object_name = 'shoes'
    paginate_by= 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = 'NIKE'
        return context

class PumaListView(ListView):
    model=Shoes
    queryset = Shoes.objects.filter(brand__iexact="puma")
    template_name = 'shoes/brand.html'
    context_object_name = 'shoes'
    paginate_by= 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = 'PUMA'
        return context

class AdidasListView(ListView):
    model=Shoes
    queryset = Shoes.objects.filter(brand__iexact="adidas")
    template_name = 'shoes/brand.html'
    context_object_name = 'shoes'
    paginate_by= 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = 'ADIDAS'
        return context

class SearchListView(ListView):
    model=Shoes
    # queryset = Shoes.objects.filter(brand__iexact="nike")
    template_name = 'shoes/search.html'
    context_object_name = 'shoes'
    paginate_by= 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = self.request.GET.get('search')
        return context
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search is None:
            search=''      
        return Shoes.objects.filter(Q(brand__icontains=search)| Q(name__icontains=search))
        
    
# def nike(request):
#     shoes=Shoes.objects.filter(brand__iexact="nike")
#     return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Nike'})


# def adidas(request):
#     shoes=Shoes.objects.filter(brand__iexact="adidas")
#     return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Adidas'})
    
# def puma(request):
#     shoes=Shoes.objects.filter(brand__iexact="puma")
#     return render(request,'shoes/brand.html',{'shoes':shoes,'brand':'Puma'})

def details(request,shoe_id):
    shoe=get_object_or_404(Shoes,pk=shoe_id)
    print(shoe.brand)
    shoes=Shoes.objects.filter(brand__icontains=shoe.brand).order_by('-date')[:3]
    context={'shoe':shoe,'allshoes':shoes}
    return render(request,'shoes/details.html',context)