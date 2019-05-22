from django.shortcuts import render
from products.models import Product

def do_search(request):
    products = Product.objects.filter(name__contains=request.GET['q'])
    return render(request, "allproducts.html", {"products": products})
