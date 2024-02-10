from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from lendloop.models import Product, Category, Order, Review, OrderProduct
from lendloop.serializers import ProductSerializer, CategorySerializer, ProductViewSerializer,\
    OrderSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from lendloop.permissions import IsOwnerOrSuperAdmin
from lendloop.filters import ProductFilter
from rest_framework.pagination import CursorPagination
from django.core.exceptions import ValidationError





class ProductViewSet(ModelViewSet):
    # foreign_key - select_related | many to many - prefetch_related
    queryset = Product.objects.all().\
        select_related("category").prefetch_related("tags").select_related("location").prefetch_related("reviews")\
        .select_related("user")
    #limits only for authenticated users
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filterset_class = ProductFilter

    pagination_class = CursorPagination

    ordering_fields = ("price")
    ordering = ("price",)

    #If we use GET method, we see all the data,
    #if we do POST, DELETE, etc we see only Product data and category id (no category details)
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductViewSerializer
        else:
            return ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrSuperAdmin)
    queryset = Order.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.filter(user=self.request.user)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Assuming a user is logged in, filter reviews by this user's orders
        user = self.request.user
        if user.is_authenticated:
            ordered_product_ids = OrderProduct.objects.filter(
                order__user=user
            ).values_list('product_id', flat=True)
            return Review.objects.filter(product__id__in=ordered_product_ids)
        # If no user is authenticated, return an empty queryset
        return Review.objects.none()

    def perform_create(self, serializer):
        # Ensure the user can only create a review for a product they have ordered
        user = self.request.user
        product_id = serializer.validated_data['product'].id
        if not OrderProduct.objects.filter(order__user=user, product_id=product_id).exists():
            raise ValidationError('You can only review products you have ordered.')
        serializer.save()