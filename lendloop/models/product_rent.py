from django.db import models
from datetime import datetime

class ProductRent(models.Model):
    rent = models.ForeignKey(
        "lendloop.Rent", on_delete=models.CASCADE,
        related_name="products_rent"
    )
    product = models.ForeignKey(
        "lendloop.Product", on_delete=models.CASCADE,
        related_name="products_rent"
    )
    date = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return f"{self.product.name} x {self.date} "

    class Meta:
        verbose_name_plural = "Product's rent"