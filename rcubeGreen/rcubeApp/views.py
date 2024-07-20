from django.core.paginator import Paginator

from usersApp.models import Product
from .models import NewsArticle, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsArticle, PaymentMethod
from .forms import PaymentMethodForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
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
    total_amount = request.POST.get('total_amount', 0)
    order = Order.objects.filter(user=request.user, status='Pending').first()

    if not order:
        return redirect('cart')  # Redirect to cart if no pending order

    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            payment_method = form.save(commit=False)
            payment_method.user = request.user
            payment_method.amount = total_amount  # Set the total amount
            payment_method.order = order  # Set the order
            payment_method.save()
            order.status = 'Processed'
            order.save()  # Update order status to prevent duplication
            return redirect('payment_successful',
                            payment_id=payment_method.id)  # Redirect to the Payment Successful page
    else:
        form = PaymentMethodForm(initial={'total_amount': total_amount})

    return render(request, 'add_payment_method.html', {'form': form, 'total_amount': total_amount})


@login_required
def payment_successful(request, payment_id):
    payment = get_object_or_404(PaymentMethod, id=payment_id, user=request.user)
    payment_time = timezone.localtime(payment.date)  # Convert to local timezone
    return render(request, 'payment_successful.html', {'payment': payment, 'payment_time': payment_time})
