from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def all_products2(request):
    products = Product.objects.all()
    return render(request, "allproducts.html", {"products": products})
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.save()
    return render(request, "productdetail.html", {'product': product})