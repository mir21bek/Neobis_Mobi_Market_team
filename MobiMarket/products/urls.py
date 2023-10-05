from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'product/api', ProductOwnerApiView, basename='product-api')
urlpatterns = [
    path('product-list/', ProductApiView.as_view()),
    path('product-list/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail'),
    path('like/<int:product_id>/', like_product, name='like-product'),
    path('unlike/<int:product_id>/', unlike_product, name='unlike-product'),
    path('like-counts/<int:product_id>/', get_like_counts, name='like-counts'),
]
urlpatterns += router.urls
