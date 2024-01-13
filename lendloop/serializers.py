from rest_framework import serializers
from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
from lendloop.models.availability import Availability
from lendloop.models.product_status import ProductStatus
from lendloop.models.subcategory import SubCategory




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','created_at','price','description','category', 'tags','location','rankings')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','description')

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ('id', 'product','date_from', 'date_to')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name")


class ProductViewSerializer(ProductSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatus
        fields = ("status", "product", "date")