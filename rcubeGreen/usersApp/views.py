from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from rcubeApp.models import Order
from .forms import ProductForm, CategoryForm, LoginForm, RegisterForm, EditProfileForm
from .models import Product, Category
from django.contrib.auth.forms import AuthenticationForm
from rcubeApp.models import OrderItem

def user_logout(request):
    logout(request)
    return redirect("/")


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


# Product Views
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('list_products')
    return render(request, 'delete_product.html', {'product': product})


@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})


# Category Views
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('list_categories')
    return render(request, 'delete_category.html', {'category': category})


@login_required
def user_profile(request):
    if 'profile_view_count' not in request.session:
        request.session['profile_view_count'] = 0
    request.session['profile_view_count'] += 1

    last_login = request.COOKIES.get('last_login')
    response = render(request, 'user_profile.html', {
        'last_login': last_login,
        'view_count': request.session['profile_view_count']
    })

    response.set_cookie('last_login', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return response


def user_accounts(request):
    form = RegisterForm()
    login_form = AuthenticationForm()
    error_message = None
    if request.method == 'POST':
        if 'signup' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('home')
                else:
                    error_message = 'Oops, your account is not active :)'
            else:
                error_message = 'Invalid login details, please try again'
    return render(request, 'user_accounts.html', {'form': form, 'login_form': login_form, 'error_message': error_message})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def user_orders(request):
    order_item = OrderItem.objects.filter(order__user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {"orders": orders, 'items': order_item})
