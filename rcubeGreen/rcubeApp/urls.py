from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_article_list_view, name='news_article_list'),
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('makepayment/', views.add_payment_method, name='makepayment'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('payment-successful/<int:payment_id>/', views.payment_successful, name='payment_successful'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

]
