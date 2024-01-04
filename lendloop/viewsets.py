from rest_framework.viewsets import ModelViewSet

from lendloop.models.product import Product
from lendloop.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer