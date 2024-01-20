from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from lendloop.models import Product, Category, Order
from lendloop.serializers import ProductSerializer, CategorySerializer, ProductViewSerializer,\
    OrderSerializer
from rest_framework.permissions import IsAuthenticated
from lendloop.permissions import IsOwnerOrSuperAdmin
from lendloop.filters import ProductFilter




class ProductViewSet(ModelViewSet):
    # foreign_key - select_related | many to many - prefetch_related
    queryset = Product.objects.all().\
        select_related("category").prefetch_related("tags").select_related("location").prefetch_related("rankings")\
        .select_related("user").prefetch_related("availabilities")
    #limits only for authenticated users
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

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
