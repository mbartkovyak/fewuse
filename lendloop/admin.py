from django.contrib import admin

from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
#from lendloop.models.ranking import Ranking

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
#admin.site.register(Ranking)