from django.contrib.auth import get_user_model
from django.db import models

from orders.models.order import Order
from products.models import Furniture

UserModel = get_user_model()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
