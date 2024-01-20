from django.contrib.auth.models import User
from rest_framework import serializers
from lendloop.models import Product, Category,Tag, Location, Order, OrderProduct
from rest_framework.authtoken.models import Token




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name','user','created_at','price','description','category', 'tags','location','rankings','availabilities')


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


class ProductViewSerializer(ProductSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)


class RegistrationSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    class Meta:
        model = User
        fields = ("username", "password", "token")


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ("product","insurance", "number_of_days")

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("id", "user","insurance", "order_products")

    def create(self, validated_data):
        order_products = validated_data.pop("order_products")
        order = Order.objects.create(**validated_data)

        order_products_items = []
        for order_product in order_products:
            order_products_items.append(
                OrderProduct(order=order, **order_product)
            )

        OrderProduct.objects.bulk_create(order_products_items)

        return order
