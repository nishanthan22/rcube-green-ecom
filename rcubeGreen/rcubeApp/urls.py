from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_article_list_view, name='news_article_list'),
]
