from django.db import models
from lendloop.models.category import Category

class SubCategory(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'SubCategories'

