from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Order


class OrderAPITests(APITestCase):
    def setUp(self):
        # Create a test customer
        self.customer = Customer.objects.create(customer_name="Test Customer", email="test@example.com")
        self.url = reverse('order-list')  # Adjust the URL name as needed

    def test_create_order_success(self):
        """Test creating an order with a valid customer and amount."""
        data = {
            "customer": self.customer.id,
            "order_amount": 1200.00  # This should apply a 10% discount
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().order_amount, 1080.00)  # Check discounted amount

    def test_create_order_customer_not_exist(self):
        """Test creating an order with a non-existent customer."""
        data = {
            "customer": 9999,  # Assuming this ID does not exist
            "order_amount": 1200.00
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Customer does not exist.", response.data["message"])

    def test_create_order_invalid_amount(self):
        """Test creating an order with a negative amount."""
        data = {
            "customer": self.customer.id,
            "order_amount": -100.00  # Invalid amount
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("order_amount", response.data["errors"])  # Check for validation error

