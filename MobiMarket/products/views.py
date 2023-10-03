from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, LikeProduct
from .serializers import ProductSerializer, LikeProductSerializer
from .utils import get_like, delete_like, get_like_count


class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_product(request):
    user = request.user
    product_id = request.data.get('product_id')

    if product_id is None:
        return Response({"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if get_like(user, product):
        return Response({"message": "Product liked successfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "Product already liked"}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unlike_product(request, product_id):
    user = request.user

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if delete_like(user, product):
        return Response({"message": "Product unliked successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Product is not liked"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def get_like_counts(request):
    like_counts = get_like_count()
    return Response(like_counts, status=status.HTTP_200_OK)
