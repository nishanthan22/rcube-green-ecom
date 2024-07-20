from django.core.paginator import Paginator

from usersApp.models import Product
from .models import NewsArticle, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsArticle, PaymentMethod
from .forms import PaymentMethodForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from django.db.models import Q
from django.utils import timezone


def news_article_list_view(request):
    articles = NewsArticle.objects.all()

    # Sorting
    sort_by = request.GET.get('sort_by', 'date_posted')
    if sort_by == 'title':
        articles = articles.order_by('title')
    else:
        articles = articles.order_by('-date_posted')

    # Filtering
    category = request.GET.get('category')
    if category:
        articles = articles.filter(category=category)

    # Pagination
    paginator = Paginator(articles, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
        'category': category,
    }
    return render(request, 'rcube-green-ecom/news_article_list.html', context)


def articles(request):
    return render(request, 'articles.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
    order_item.save()
    order.update_total_price()
    return redirect('shop')

@login_required
def cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            order_item = get_object_or_404(OrderItem, id=item_id, order__user=request.user, order__status='Pending')
            order_item.delete()
            order_item.order.update_total_price()
            return redirect('cart')

    order = Order.objects.filter(user=request.user, status='Pending').first()
    if not order:
        order_items = []
        total_price = 0
    else:
        order_items = order.orderitem_set.all()
        total_price = order.total_price
    return render(request, 'cart.html', {'order_items': order_items, 'total_price': total_price})




def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def home(request):
    if request.user.is_superuser:
        return render(request, 'admin_home.html')
    else:
        return render(request, 'home.html')


def search(request):
    query = request.GET.get('q')
    results = []  # Replace with your actual search logic to get results

    # Example logic to populate results
    if query:
        # Perform search in your database or data source
        results = ["Result 1", "Result 2", "Result 3"]  # Replace with actual search results

    return render(request, 'search.html', {'query': query, 'results': results})


@login_required
def add_payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            payment_method = form.save(commit=False)
            payment_method.user = request.user
            payment_method.save()
            return redirect('payment_list')
    else:
        form = PaymentMethodForm()
    return render(request, 'add_payment_method.html', {'form': form})


@login_required
def payment_history(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'date')

    payments = PaymentMethod.objects.filter(user=request.user)

    if search_query:
        payments = payments.filter(
            Q(description__icontains=search_query) |
            Q(amount__icontains=search_query) |
            Q(method__icontains=search_query)
        )

    if sort_by == 'amount':
        payments = payments.order_by('amount')
    else:
        payments = payments.order_by('-date')

    paginator = Paginator(payments, 10)  # Show 10 payments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }

    return render(request, 'payment_list.html', context)


@login_required
def export_payments_to_csv(request):
    payments = PaymentMethod.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="payments.csv"'

    writer = csv.writer(response)
    writer.writerow(['Amount', 'Method', 'Date', 'Description'])

    for payment in payments:
        writer.writerow([payment.amount, payment.method, payment.date, payment.description])

    return response


@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    if request.method == 'POST':
        if order:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            name_on_card = request.POST.get('name_on_card')
            card_number = request.POST.get('card_number')
            exp_month = request.POST.get('exp_month')
            exp_year = request.POST.get('exp_year')
            cvv = request.POST.get('cvv')

            # Calculate total amount from order items
            total_amount = order.total_price

            # Save payment method
            payment = PaymentMethod(
                user=request.user,
                amount=total_amount,
                date=timezone.now(),
                method='Credit Card',
                full_name=full_name,
                email=email,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                name_on_card=name_on_card,
                card_number=card_number,
                exp_month=exp_month,
                exp_year=exp_year,
                cvv=cvv,
            )
            payment.save()

            # Update order status
            order.status = 'Processed'
            order.completed = timezone.now()
            order.save()
            return redirect('payment_list')

    return render(request, 'checkout.html', {'order': order})