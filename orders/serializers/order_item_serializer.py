from rest_framework import serializers

from orders.models import OrderItem
from products.models import Furniture
from products.serializers import FurnitureSerializer


class CreateOrderItemSerializer(serializers.ModelSerializer):
    furniture = serializers.PrimaryKeyRelatedField(queryset=Furniture.objects.all())

    class Meta:
        model = OrderItem
        fields = ('furniture', 'quantity')


class ReadOrderItemSerializer(serializers.ModelSerializer):
    furniture = FurnitureSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('furniture', 'quantity')
