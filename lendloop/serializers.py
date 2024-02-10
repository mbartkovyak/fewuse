from django.contrib.auth.models import User
from rest_framework import serializers
from lendloop.models import Product, Category,Tag, Location, Order, OrderProduct, Review
from rest_framework.authtoken.models import Token




class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = ('id', 'name','user','created_at','price','description','category', 'tags','location')

    def create(self, validated_data):
        # Extract many-to-many fields data
        tags_data = validated_data.pop('tags', None)

        # Create the Product instance without many-to-many fields
        product = Product.objects.create(**validated_data)

        # Set the many-to-many relationships after the instance is created
        if tags_data is not None:
            product.tags.set(tags_data)

        return product


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
        fields = ("product", "start_date", "end_date", "rental_period_length")

    def get_rental_period_length(self, obj):
        return obj.rental_period_length()

    def validate(self, data):
        """
        Perform various validations:
        - Check that the start_date is before the end_date.
        - Check that the product is not already booked for the given date range.
        """
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("The end date must be after the start date.")

        product_id = data['product']
        start_date = data['start_date']
        end_date = data['end_date']

        # Check for overlapping bookings
        overlapping_orders = Order.objects.filter(
            order_products__product=product_id,
            order_products__start_date__lt=end_date,
            order_products__end_date__gt=start_date
        )

        if overlapping_orders.exists():
            raise serializers.ValidationError(
                f"Product {product_id} is already booked in the given date range."
            )

        return data

class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("id", "user", "insurance", "order_products")

    def create(self, validated_data):
        order_products_data = validated_data.pop("order_products")
        order = Order.objects.create(**validated_data)

        order_products_instances = []
        for product_data in order_products_data:
            # Notice we're not popping insurance from product_data anymore
            order_products_instances.append(OrderProduct(order=order, **product_data))

        OrderProduct.objects.bulk_create(order_products_instances)

        return order


class ProductViewSerializer(ProductSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        # Specify the fields that you want to include in the serialized output
        fields = ['id', 'name', 'price', 'category', 'tags', 'location', 'user', 'reviews']


class ReviewSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField to display product names instead of IDs
    product = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Product.objects.none()  # Default queryset, will be overridden
    )

    class Meta:
        model = Review
        fields = ['id', 'stars', 'comment', 'product']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user = self.context['request'].user
        if user.is_authenticated:
            # Set the queryset for 'product' field to products that the user has ordered
            self.fields['product'].queryset = Product.objects.filter(
                order_products__order__user=user
            ).distinct()



