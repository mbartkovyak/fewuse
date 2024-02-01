from django.db import models
from lendloop.models.insurance import Insurance


class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='order', blank=True, null=True)

    def __str__(self):
        return f"id = {str(self.id)}"

