from django.shortcuts import render


def index(request):
    """View to display index.html"""
    return render(request, "index.html")