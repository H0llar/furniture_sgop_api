from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from authentication.permissions import IsManagerOrReadonly
from products.models import Brand
from products.serializers import BrandSerializer


@extend_schema(tags=['Brands'])
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsManagerOrReadonly]
