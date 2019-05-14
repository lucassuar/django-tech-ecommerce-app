from django.shortcuts import render


def about(request):
    """View to display about.html"""
    return render(request, "about.html")