from decimal import Decimal

class OrderService:
    @staticmethod
    def calculate_discount(order_amount):
        if not isinstance(order_amount, Decimal) and Decimal(order_amount) < 0:
            raise ValueError("order_amount must be a Decimal.")
        # Check if order_amount is greater than $1000 and apply a 10% discount
        if order_amount > Decimal('1000.00'):
            return order_amount * Decimal('0.9')  # Apply a 10% discount
        return order_amount
