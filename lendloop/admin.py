from django.contrib import admin

from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
from lendloop.models.ranking import Ranking
from lendloop.models.availability import Availability
from lendloop.models.status import Status
from lendloop.models.product_status import ProductStatus
from lendloop.models.subcategory import SubCategory


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Ranking)
admin.site.register(Availability)
admin.site.register(Status)
admin.site.register(ProductStatus)
admin.site.register(SubCategory)