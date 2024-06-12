import django_filters

from products.models import Furniture


class FurnitureFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Furniture
        fields = ('brand', 'category', 'name', 'price')
