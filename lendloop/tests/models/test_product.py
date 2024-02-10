from django.test import TestCase
from django.contrib.auth.models import User
from lendloop.models import Product, Order, OrderProduct
from datetime import date

class BaseTest(TestCase):
    def setUp(self):
        # Create a user instance for testing
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create a product instance
        self.product = Product.objects.create(
            name='Test Product',
            price=100,
            user=self.user
        )

        # Create order instance
        self.order = Order.objects.create(user=self.user)

        # Create order products with different date ranges
        OrderProduct.objects.create(
            order=self.order,
            product=self.product,
            start_date=date(2024, 1, 1),
            end_date=date(2024, 1, 10)
        )
        OrderProduct.objects.create(
            order=self.order,
            product=self.product,
            start_date=date(2024, 2, 1),
            end_date=date(2024, 2, 10)
        )

#test_products is testing availability of the product in the given period
class ProductAvailabilityTestCase(BaseTest):

    def test_product_availability(self):
        # Test a date range when the product is already booked
        result = self.product.is_available(date(2024, 1, 5), date(2024, 1, 15))
        print(f"Testing availability for Jan 5, 2024, to Jan 15, 2024 when it is already booked:Result: {result}")
        self.assertFalse(result)
"""
        # Test a date range when the product is not booked
        self.assertTrue(self.product.is_available(date(2024, 1, 11), date(2024, 1, 31)))

        # Test a date range overlapping with another booking at the start
        self.assertFalse(self.product.is_available(date(2024, 1, 10), date(2024, 1, 20)))

        # Test a date range overlapping with another booking at the end
        self.assertFalse(self.product.is_available(date(2024, 2, 25), date(2024, 3, 5)))

        # Test a date range completely outside any bookings
        self.assertTrue(self.product.is_available(date(2024, 3, 11), date(2024, 3, 20)))
"""