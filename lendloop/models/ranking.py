from django.db import models
from django.core.exceptions import ValidationError

def non_negative_validator(value):
    if value < 1 or value > 5 :
        raise ValidationError('Ranking can be from 1 to 5')

class Ranking(models.Model):
    stars = models.FloatField(validators=[non_negative_validator])
    comment = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Rankings'

