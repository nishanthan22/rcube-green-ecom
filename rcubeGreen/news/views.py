import math
import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import quote
from .models import Article, Source
from django.db.models import Q
from datetime import datetime


def fetch_destinations(request, page):
    limit = 20
    api_key = "3266f877bb2749a3955f4f8c87c10de0"
    query = "environment"

    # Get filter parameters from the request
    source_name = request.GET.get('source_name')
    author = request.GET.get('author')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    keyword = request.GET.get('keyword')

    # # Construct the base API URL
    # api_url = (f"https://newsapi.org/v2/everything?q={quote(query)}"
    #            f"&apiKey={api_key}&pageSize={limit}&page={page}")
    #
    # # Fetch data from the API
    # response = requests.get(api_url)
    # if response.status_code != 200:
    #     return HttpResponse("Failed to fetch data from the API.", status=response.status_code)

    # data = response.json()
    # count = data.get('totalResults')
    total_pages = math.ceil(100 / limit)

    # Print the fetched data for debugging
    # print(json.dumps(data, indent=4))

    # Fetch and save articles
    fetch_and_save_destinations(page, limit)

    # Apply filters to the fetched articles
    filtered_articles = Article.objects.all()

    if source_name:
        filtered_articles = filtered_articles.filter(source__name__icontains=source_name)

    if author:
        filtered_articles = filtered_articles.filter(author__icontains=author)

    if start_date:
        filtered_articles = filtered_articles.filter(publishedAt__gte=datetime.strptime(start_date, '%Y-%m-%d'))

    if end_date:
        filtered_articles = filtered_articles.filter(publishedAt__lte=datetime.strptime(end_date, '%Y-%m-%d'))

    if keyword:
        filtered_articles = filtered_articles.filter(
            Q(title__icontains=keyword) | Q(description__icontains=keyword)
        )
        # Turn off pagination if filtering by keyword
        filtered_articles = list(filtered_articles)
        unique_articles = []
        seen = set()
        for article in filtered_articles:
            identifier = (article.author, article.publishedAt, article.title)
            if identifier not in seen:
                seen.add(identifier)
                unique_articles.append(article)
        page_data = unique_articles
        total_pages = 1
    else:
        # Paginate the filtered results
        offset = (page - 1) * limit
        filtered_articles = list(filtered_articles)
        unique_articles = []
        seen = set()
        for article in filtered_articles:
            identifier = (article.author, article.publishedAt, article.title)
            if identifier not in seen:
                seen.add(identifier)
                unique_articles.append(article)
        page_data = unique_articles[offset:offset + limit]

    return render(request, 'news/index.html', {
        'destinations': page_data,
        'curr_page': page,
        "total_pages": total_pages
    })


def fetch_and_save_destinations(page=1, limit=20):
    api_key = "3266f877bb2749a3955f4f8c87c10de0"
    query = "environment"
    api_url = (f"https://newsapi.org/v2/everything?q={quote(query)}"
               f"&apiKey={api_key}&pageSize={limit}&page={page}")

    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to fetch data from the API. Status code: {response.status_code}")
        return []

    data = response.json()
    articles_data = data.get('articles', [])

    # Print the fetched articles data for debugging
    print(json.dumps(articles_data, indent=4))

    # List to hold Article instances
    articles = []
    for item in articles_data:
        source_name = item.get('source', {}).get('name', 'Unknown')
        source, _ = Source.objects.get_or_create(name=source_name)

        article = Article(
            source=source,
            author=item.get('author', 'Unknown'),
            title=item.get('title', 'No Title'),
            description=item.get('description', 'No Description'),
            url=item.get('url', 'No URL'),
            urlToImage=item.get('urlToImage', 'No Image URL'),
            publishedAt=item.get('publishedAt', '1970-01-01T00:00:00Z'),
            content=item.get('content', 'No Content')
        )
        articles.append(article)

    # Bulk create articles, ignoring conflicts
    try:
        Article.objects.bulk_create(articles, ignore_conflicts=True)
        return articles
    except Exception as e:
        print(f"Error during database operation: {e}")
        return []
