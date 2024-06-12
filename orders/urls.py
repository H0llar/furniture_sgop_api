from django.urls import include, path
from rest_framework import routers

from orders.viewsets import OrderViewSet

app_name = 'orders'

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path(r'', include(router.urls)),
]
