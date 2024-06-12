from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from authentication.permissions import IsManagerOrReadonly
from products.filters import FurnitureFilter
from products.models import Furniture
from products.serializers import FurnitureSerializer


@extend_schema(tags=['Furniture'])
class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [IsManagerOrReadonly]
    filterset_class = FurnitureFilter
