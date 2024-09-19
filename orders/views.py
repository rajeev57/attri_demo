from django.core.serializers import serialize
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .service import OrderService

class CustomerViewSet(APIView):
    def get(self, request, customer_id=None):
        if customer_id is not None:
            customer = get_object_or_404(Customer, id=customer_id)
            serializer = CustomerSerializer(customer)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({"status": "success", "data":  serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return Response({"status": "success", "message": "Order deleted successfully."},status=status.HTTP_204_NO_CONTENT)


class OrderViewSet(APIView):
    def get(self, request, order_id=None):
        if order_id is not None:
            # Use get_object_or_404 to retrieve the order or raise a 404 error
            order = get_object_or_404(Order, id=order_id)
            serializer = OrderSerializer(order)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # Retrieve all orders
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        customer_id = request.data.get('customer')
        # Ensure customer exists using exists()
        if not Customer.objects.filter(id=customer_id).exists():
            return Response({"status": "error", "message": "Customer does not exist."},status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_amount = serializer.validated_data['order_amount']
            discount_amount = OrderService.calculate_discount(order_amount)
            serializer.validated_data['order_amount'] = discount_amount
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return Response({"status": "success", "message": "Order deleted successfully."},status=status.HTTP_204_NO_CONTENT)





