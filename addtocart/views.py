from django.shortcuts import render

from .models import Product

# Create your views here.
def addtocart(request):
    data = Product.objects.all()
    return render(request , 'addtocart.html', {"data" : data})

