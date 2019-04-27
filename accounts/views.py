from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    """Index.html file return"""
    return render(request,  'index.html')
    
def logout(request):
    """Logout the user"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    """Login page return"""
    return render(request, 'login.html')