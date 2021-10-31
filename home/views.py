from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "index.html")

def products(request):
    productss = Product.objects.all()
    return render(request, "products.html", {'productss':productss})
    
def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
