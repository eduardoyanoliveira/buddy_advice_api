from rest_framework.viewsets import ModelViewSet
from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
