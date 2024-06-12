import django_filters

from products.models import Brand


class BrandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='startswith')

    class Meta:
        model = Brand
        fields = ('name',)
