from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(
        "lendloop.Status", through="lendloop.ProductStatus", related_name='products_for_status'
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Statuses'