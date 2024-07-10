from django.urls import path
from .views import articles, shop, cart, about, contact, home

urlpatterns = [
    path('home/', home, name='home'),
    path('articles/', articles, name='articles'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
