from django.db.models import Sum, F
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from authentication.permissions import IsManager
from orders.filters import OrderFilter
from orders.models import Order, OrderItem
from orders.permissions import IsOrderOwner
from orders.serializers import CreateOrderSerializer, OrderStatusSerializer, OrderSummarySerializer
from orders.serializers.order_serializer import ReadOrderSerializer


@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filterset_class = OrderFilter

    @extend_schema(parameters=[
        OpenApiParameter(name='status',
                         type=OpenApiTypes.STR,
                         location=OpenApiParameter.QUERY,
                         enum=['DV', 'PD', 'SP']),
    ])
    @action(methods=['GET'], detail=False)
    def my(self, request):
        orders = Order.objects.filter(user=request.user)
        filtered = OrderFilter(request.GET, queryset=orders)
        serializer = ReadOrderSerializer(filtered.qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses={200: OrderSummarySerializer})
    @action(methods=['GET'], detail=False)
    def summary(self, request):
        serializer = OrderSummarySerializer({
            'total_orders': Order.objects.all().count(),
            'total_earnings': OrderItem.objects.annotate(
                total_price=F('quantity') * F('furniture__price')
            ).aggregate(total=Sum('total_price'))['total']
        })
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses={200: OrderStatusSerializer})
    @action(methods=['GET'], detail=False)
    def status(self, request):
        serializer = OrderStatusSerializer({
            'pending_orders': Order.objects.filter(status=Order.Status.PENDING).count(),
            'shipped_orders': Order.objects.filter(status=Order.Status.SHIPPED).count(),
            'delivered_orders': Order.objects.filter(status=Order.Status.DELIVERED).count()
        })
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        return ReadOrderSerializer if self.request.method in SAFE_METHODS else CreateOrderSerializer

    def get_permissions(self):
        if self.action in ['create', 'my']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated & IsOrderOwner]
        else:
            permission_classes = [IsManager]
        return [permission() for permission in permission_classes]
