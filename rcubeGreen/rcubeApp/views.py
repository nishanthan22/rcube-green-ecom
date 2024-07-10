from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def articles(request):
    return render(request, 'articles.html')

def shop(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# views.py

def home(request):
    return render(request, 'home.html')

