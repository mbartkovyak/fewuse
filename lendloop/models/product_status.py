from django.db import models
from datetime import datetime

class ProductStatus(models.Model):
    status = models.ForeignKey(
        "lendloop.Status", on_delete=models.CASCADE,
        related_name="products_status"
    )
    product = models.ForeignKey(
        "lendloop.Product", on_delete=models.CASCADE,
        related_name="products_status"
    )
    date = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return f"{self.product.name} x {self.status} "

    class Meta:
        verbose_name_plural = "Product's status"