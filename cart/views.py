from django.shortcuts import render, redirect, reverse
from products.models import Product

# Create your views here.
def view_cart(request):
    """A View that shows the cart details page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    products = Product.objects.all()
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect('/products_list/', {'products': products})


def adjust_cart(request, id):
    """
    Change quantity of a product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))