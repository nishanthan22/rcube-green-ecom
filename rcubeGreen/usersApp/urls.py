# urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.user_login),
    path("logout", views.user_logout),
    path('add_category/', views.add_category, name='add_category'),
    path('categories/', views.list_categories, name='list_categories'),
    path('add_product/', views.add_product, name='add_product'),
    path('products/', views.list_products, name='list_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
