from rest_framework.viewsets import ModelViewSet

from lendloop.models import Product, Category
from lendloop.models.availability import Availability
from lendloop.serializers import ProductSerializer, CategorySerializer, ProductViewSerializer, AvailabilitySerializer
from rest_framework.permissions import IsAuthenticated




class ProductViewSet(ModelViewSet):
    # foreign_key - select_related | many to many - prefetch_related
    queryset = Product.objects.all().\
        select_related("category").prefetch_related("tags").select_related("location").prefetch_related("rankings").select_related("user")
    #limits only for authenticated users
    permission_classes = (IsAuthenticated,)

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

class AvailabilityViewSet(ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = (IsAuthenticated,)


