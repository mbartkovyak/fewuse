from django.core.exceptions import ValidationError
from django.db import models
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
from lendloop.models.review import Review
from django.db.models import Q

def non_negative_validator(value):
    if value <= 0:
        raise ValidationError('Price cannot be negative')



class Product(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(validators=[non_negative_validator])
    description = models.CharField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    orders = models.ManyToManyField(
        "lendloop.Order", through="lendloop.OrderProduct"
    )


    def is_available(self, start_date, end_date):
        # Check if there are any order_products that overlap with the requested dates
        overlapping_orders = self.order_products.filter(
            Q(start_date__lte=end_date) & Q(end_date__gte=start_date)
        )
        return not overlapping_orders.exists()

    def __str__(self):
        return self.name

