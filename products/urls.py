from django.urls import include, path
from rest_framework import routers

from products.viewsets import FurnitureViewSet, CategoryViewSet, BrandViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'furniture', FurnitureViewSet, basename='furniture')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'brands', BrandViewSet, basename='brands')

urlpatterns = [
    path('', include(router.urls)),
]
