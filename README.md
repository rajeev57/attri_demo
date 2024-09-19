# Order Management System
order_management/
│
├── order_management/           # Main project folder
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Project URLs
│   ├── asgi.py                 # ASGI configuration
│   └── wsgi.py                 # WSGI configuration
│
├── orders/                     # Django app for orders
│   ├── migrations/             # Database migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                # Admin configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Models for Customer, Product, Order
│   ├── serializers.py          # Serializers for the models
│   ├── tests.py                # Tests for the app
│   └── views.py                # Viewsets for the API
│
├── manage.py                   # Django's command-line utility
├── requirements.txt        # Place your dependencies here
├── Dockerfile              # Place Dockerfile here
└── docker-compose.yml 
# Project documentation
A simple order management system built with Django and Django REST Framework. This application allows you to manage customers, products, and orders through a RESTful API, backed by a PostgreSQL database.

## Features

- **Customer Management**: Create, retrieve, update, and delete customers.
- **Order Management**: Create and manage orders, linking customers to products.

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL
- Python

## Prerequisites
- Python 3.x
- PostgreSQL
- pip (Python package manager)

## Installation

# Order Management System

A simple order management system built with Django and Django REST Framework. 

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Configure the PostgreSQL database in `settings.py`.
5. Run migrations: `python manage.py migrate`.
6. Create a superuser: `python manage.py createsuperuser`.
7. Run the server: `python manage.py runserver`.

## API Endpoints

- `POST /api/customers/`
- `GET /api/customers/{customer_id}/`
- `GET /api/customers/`
- `POST /api/orders/`
- `GET /api/orders/{order_id}/`
- `DELETE /api/orders/{order_id}/`

## To apply database migration
python manage.py makemigrations
python manage.py migrate

## to run or create superuser
python manage.py createsuperuser

# For login admin path
http://127.0.0.1:8000/admin/auth/user/
## Super user 
rajee 
## password
admin

## To run the server
python manage.py runserver

## To test case:-
python manage.py test orders

## Local host url:-
# For customers :- 
http://127.0.0.1:8000/api/customers/
# For order :- 
http://127.0.0.1:8000/api/orders/

