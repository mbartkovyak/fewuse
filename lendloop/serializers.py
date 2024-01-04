from rest_framework import serializers
from lendloop.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','created_at','updated_at','price','description')
