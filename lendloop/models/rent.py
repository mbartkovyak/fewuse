from django.db import models


class Rent(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    in_rent = models.BooleanField()
    product = models.ManyToManyField("lendloop.Product", through="lendloop.ProductRent", related_name='products_for_rent')
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"{self.product.name} x {self.date_from} x {self.date_to}"


    class Meta:
        verbose_name_plural = 'Rents'