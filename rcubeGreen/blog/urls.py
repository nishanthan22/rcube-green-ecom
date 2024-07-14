from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    GreenInnovationList,
    EcoProductsList,
    SustainableLivingList,
    GreenInnovationDetail,
    EcoProductsDetail,
    SustainableLivingDetail,
)
app_name = 'blog'

urlpatterns = [
    path('green_innovation/', GreenInnovationList.as_view(), name='green_innovation_posts'),
    path('eco_products/', EcoProductsList.as_view(), name='eco_products_posts'),
    path('sustainable_living/', SustainableLivingList.as_view(), name='sustainable_living_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('green_innovation/<slug:slug>/', GreenInnovationDetail.as_view(), name='green_innovation_detail'),
    path('eco_products/<slug:slug>/', EcoProductsDetail.as_view(), name='eco_products_detail'),
    path('sustainable_living/<slug:slug>/', SustainableLivingDetail.as_view(), name='sustainable_living_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)