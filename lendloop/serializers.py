from django.contrib.auth.models import User
from rest_framework import serializers
from lendloop.models import Product, Category,Tag, Location, Availability, ProductRent
from rest_framework.authtoken.models import Token




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','user','created_at','price','description','category', 'tags','location','rankings')


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

class ProductRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRent
        fields = ("rent", "product", "date")


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ("username", "password", "token")

class RentSerializer(serializers.ModelSerializer):
    rent_product = ProductRentSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())