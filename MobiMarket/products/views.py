from rest_framework import viewsets
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer, LikeProductSerializer


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(available=True)
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self, request=None):
        if request and 'like' in request.data:
            return LikeProductSerializer
        return self.serializer_class
