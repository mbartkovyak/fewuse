from django.db import models

class Location(models.Model):
    location = models.TextField(blank=False)
    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.location

