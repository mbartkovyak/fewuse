from django.db import models


class Insurance(models.Model):
    insurance_type = models.CharField(max_length=255)
    cost = models.FloatField()

    def __str__(self):
        return self.insurance_type