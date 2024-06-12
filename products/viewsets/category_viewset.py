from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from authentication.permissions import IsManagerOrReadonly
from products.models import Category
from products.serializers import CategorySerializer


@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrReadonly]
