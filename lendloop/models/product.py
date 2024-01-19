from django.core.exceptions import ValidationError
from django.db import models
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
from lendloop.models.ranking import Ranking

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError('Price cannot be negative')



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateField()
    price = models.FloatField(validators=[non_negative_validator])
    description = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    rankings = models.ManyToManyField(Ranking, related_name="products", blank=True)
    orders = models.ManyToManyField(
        "lendloop.Order", through="lendloop.OrderProduct"
    )

    def __str__(self):
        return self.name