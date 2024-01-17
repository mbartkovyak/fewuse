from django.contrib import admin
from lendloop.models import Product, Category,Tag, Location, Ranking, SubCategory, Availability
#ProductRent, Rent


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Ranking)
admin.site.register(Availability)
#admin.site.register(Rent)
#admin.site.register(ProductRent)
admin.site.register(SubCategory)