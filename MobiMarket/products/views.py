from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response

from .models import Product, LikeProduct
from .serializers import ProductSerializer, LikeProductSerializer
from .utils import get_like, delete_like, get_like_count


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(available=True)
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self, request=None):
        if request and 'like' in request.data:
            return LikeProductSerializer
        return self.serializer_class


class LikeApiView(generics.GenericAPIView):
    serializer_class = LikeProductSerializer

    @staticmethod
    def get(request, pk):
        user = request.user
        product = LikeProduct.objects.get(pk=pk)
        like_product = get_like(user, product)
        remove_like = delete_like(user, product)
        like_count = get_like_count()

        data = {
            'like_product': like_product,
            'remove_like': remove_like,
            'like_count': like_count
        }

        return Response(data, status=status.HTTP_200_OK)

    @classmethod
    def get_extra_actions(cls):
        return []

