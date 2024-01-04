from django.contrib import admin

from lendloop.models.product import Product
from lendloop.models.category import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)