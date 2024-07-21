from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('<int:page>/', views.fetch_destinations, name='index'),
]