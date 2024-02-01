from django.db import models



class OrderProduct(models.Model):
    order = models.ForeignKey(
        "lendloop.Order", on_delete=models.CASCADE,
        related_name="order_products"
    )
    product = models.ForeignKey(
        "lendloop.Product", on_delete=models.CASCADE,
        related_name="order_products"
    )
    insurance = models.ForeignKey(
        "lendloop.insurance", on_delete=models.CASCADE,
        related_name="order_insurance"
    )
    number_of_days = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} x {self.number_of_days}"


