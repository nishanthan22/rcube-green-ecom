from datetime import datetime
from sqlite3 import IntegrityError

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rcubeApp.models import Order
from .forms import ProductForm, CategoryForm, LoginForm, RegisterForm, EditProfileForm
from .models import Product, Category
from django.contrib.auth.forms import AuthenticationForm
from rcubeApp.models import OrderItem
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


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
    selected_category = request.GET.get('category')
    if selected_category:
        products = Product.objects.filter(category_id=selected_category)
    else:
        products = Product.objects.all()

    all_categories = Category.objects.all()
    return render(request, 'list_products.html', {
        'products': products,
        'all_categories': all_categories,
        'selected_category': selected_category
    })


# Product Views
@login_required
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


@login_required
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
    selected_category = request.GET.get('category', '')  # Getting the selected category from the URL parameters

    if selected_category:
        categories = Category.objects.filter(id=selected_category)  # Filtering by category
    else:
        categories = Category.objects.all()

    # including all categories for the filter options
    all_categories = Category.objects.all()

    return render(request, 'list_categories.html', {
        'categories': categories,
        'all_categories': all_categories,
        'selected_category': selected_category
    })


# Category Views
@login_required
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


@login_required
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
    error_messages = []

    if request.method == 'POST':
        if 'signup' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            elif form.errors:
                error_message = form.errors.as_text()
                for field, errors in form.errors.items():
                    for error in errors:
                        error_messages.append(f"{error}")

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
                    error_messages.append(error_message)
            else:
                error_message = 'Invalid login details, please try again'
                error_messages.append(error_message)

    return render(request, 'user_accounts.html',
                  {'form': form, 'login_form': login_form, 'error_message': error_message, 'error_messages': error_messages})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                return redirect('profile')
            except IntegrityError:
                form.add_error('email', 'Email is already in use.')
        else:
            if not form.has_changed():
                form.add_error(None, 'Alter any one field')
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def user_orders(request):
    order_item = OrderItem.objects.filter(order__user=request.user)
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {"orders": orders, 'items': order_item})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
