from rest_framework import serializers
from lendloop.models.product import Product
from lendloop.models.category import Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','created_at','updated_at','price','description','category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','description')
