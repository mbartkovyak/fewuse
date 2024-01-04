from django.core.exceptions import ValidationError
from django.db import models
from lendloop.models.category import Category

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError('Price cannot be negative')



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateField()
    updated_at = models.DateField()
    price = models.FloatField(validators=[non_negative_validator])
    description = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    def __str__(self):
        return self.name