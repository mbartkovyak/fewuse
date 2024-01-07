from rest_framework.viewsets import ModelViewSet

from lendloop.models.product import Product
from lendloop.models.category import Category
from lendloop.serializers import ProductSerializer, CategorySerializer, ProductViewSerializer, TagSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().\
        select_related("category").prefetch_related("tags")

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

