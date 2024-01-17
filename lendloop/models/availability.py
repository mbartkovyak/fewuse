from django.db import models
from lendloop.models.product import Product

class Availability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='availability', blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()

    class Meta:
        verbose_name_plural = "Availabilities"

    def __str__(self):
        return f"{self.date_from} x {self.date_to}"

