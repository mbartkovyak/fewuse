from django.contrib import admin
from lendloop.models import Product, Category,Tag, Location, Availability, ProductStatus, Ranking, Status, SubCategory


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