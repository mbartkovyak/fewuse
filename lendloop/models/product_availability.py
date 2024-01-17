'''from django.db import models

class ProductAvailabilty(models.Model):
    availabilty = models.ForeignKey(
        "lendloop.Availability", on_delete=models.CASCADE,
        related_name="availabilty_product"
    )
    product = models.ForeignKey(
        "lendloop.Product", on_delete=models.CASCADE,
        related_name="availabilty_product"
    )
    def __str__(self):
        return f"{self.product.name} x {self.date_from}"

    class Meta:
        verbose_name_plural = "Availabilities of products"'''
