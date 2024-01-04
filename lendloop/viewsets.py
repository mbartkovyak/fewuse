from rest_framework.viewsets import ModelViewSet

from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.serializers import ProductSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer