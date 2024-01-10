from rest_framework import serializers
from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.models.tag import Tag
from lendloop.models.location import Location
#from lendloop.models.ranking import Ranking


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','created_at','updated_at','price','description','category', 'tags','location')

#,'rankings')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name','description')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name")

"""class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ("id", "stars", "comment")"""


class ProductViewSerializer(ProductSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)


#rankings = RankingSerializer(many=True)