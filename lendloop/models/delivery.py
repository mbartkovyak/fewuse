from django.db import models


class Delivery(models.Model):
    delivery_type = models.CharField(
        max_length=60,
        default="STANDARD",
    )


    def __str__(self):
        return self.delivery_type

    class Meta:
        verbose_name_plural = 'Deliveries'