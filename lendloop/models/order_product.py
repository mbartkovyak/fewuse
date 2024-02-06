from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError



class OrderProduct(models.Model):
    order = models.ForeignKey(
        "lendloop.Order", on_delete=models.CASCADE,
        related_name="order_products"
    )
    product = models.ForeignKey(
        "lendloop.Product", on_delete=models.CASCADE,
        related_name="order_products"
    )
    start_date = models.DateField()  # Rental period start date
    end_date = models.DateField()    # Rental period end date

    def rental_period_length(self):
        # Calculate the length of the rental period
        return (self.end_date - self.start_date).days + 1  # Including both start and end dates

    def __str__(self):
        return f"{self.product.name} ({self.start_date} to {self.end_date})"


