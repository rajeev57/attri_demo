from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'email']
        extra_kwargs = {
            'customer_name': {'required': True},
            'email': {'required': True}
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_amount', 'order_date']
        extra_kwargs = {
            'order_amount': {'required': True}
        }

    def validate_order_amount(self, value):
        """Check that the order amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Order amount must be greater than zero.")
        return value
