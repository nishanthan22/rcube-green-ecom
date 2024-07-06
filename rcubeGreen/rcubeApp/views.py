from django.shortcuts import render
from django.core.paginator import Paginator
from .models import NewsArticle

def home_view(request):
    return render(request, 'rcubeApp/home.html')

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'rcubeApp/product_list.html', {'products': products})

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
