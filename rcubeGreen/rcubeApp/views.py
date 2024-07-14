from django.core.paginator import Paginator
from .models import NewsArticle
from django.shortcuts import render, redirect
from .models import NewsArticle, Payment, PaymentMethod
from .forms import PaymentMethodForm
from django.contrib.auth.decorators import login_required


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
    return render(request, 'shop.html')


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def home(request):
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
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payment_list.html', {'payments': payments})

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

