import django_filters

from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ('status',)
