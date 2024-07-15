from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_article_list_view, name='news_article_list'),
    path('home/', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('add-payment-method/', views.add_payment_method, name='add_payment_method'),
    path('payment-history/', views.payment_history, name='payment_history'),
    path('export-payments-to-csv/', views.export_payments_to_csv, name='export_payments_to_csv'),
]
