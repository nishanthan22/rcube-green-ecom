from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/', views.list_products, name='list_products'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/', views.list_categories, name='list_categories'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('user_profile/', views.user_profile, name='profile'),
    path('register/', views.user_accounts, name='register'),
    path('login/', views.user_accounts, name='login'),
    path('user_accounts/', views.user_accounts, name='user_accounts'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/user/orders/', views.user_orders, name='user_orders'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
