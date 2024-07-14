from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, CategoryForm
from .models import Product, Category


# Create your views here.
def user_login(request):
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("/")


#@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


#@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


#@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


#@login_required
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})

# Added to test payment feature
@login_required
def profile(request):
    return render(request, 'profile.html')