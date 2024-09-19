from tkinter.font import names

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .serializers import OrderSerializer
from .views import CustomerViewSet, OrderViewSet


urlpatterns = [
    path('customers/', CustomerViewSet.as_view()),
    path('customers/<int:customer_id>', CustomerViewSet.as_view()),
    path('orders/', OrderViewSet.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderViewSet.as_view()),
]
