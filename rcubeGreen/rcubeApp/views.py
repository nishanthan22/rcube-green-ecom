from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import NewsArticle
from .forms import NewsArticleForm


def add_article_view(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_article_list')
    else:
        form = NewsArticleForm()
    return render(request, 'rcubeApp/add_article.html', {'form': form})

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
    return render(request, 'rcubeApp/news_article_list.html', context)
