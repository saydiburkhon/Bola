from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def about(request):
    return render (request, 'about.html', {})

def contact(request):
    return render (request, 'contact.html', {})

def packages(request):
    return render (request, 'packages.html', {})

def pricing(request):
    return render (request, 'pricing.html', {})
