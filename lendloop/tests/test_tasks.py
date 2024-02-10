from datetime import date, timedelta

from django.test import TestCase
from unittest.mock import patch, Mock
from django.contrib.auth.models import User
from lendloop.models import Order, Product, OrderProduct, Insurance
from lendloop.tasks import order_created_task
from lendloop.tests.models.test_product import BaseTest

class OrderCreatedTaskTestCase(BaseTest):

    @patch("lendloop.tasks.send_mail")
    def test_order_created_task(self, mock_send_mail):
        # Call the task
        order_created_task(self.order.id)

        # Check that send_mail was called at least once
        mock_send_mail.assert_called()

        # If you still want to ensure some basic details, like the subject or recipient:
        mock_send_mail.assert_called_with(
            "New Order",
            Mock(),  # Mock() here means "don't care about the exact content"
             "mbartkovyak@gmail.com",
             [self.user.email],
             html_message=Mock()  # Again, Mock() means "don't care about the exact content"
        )
