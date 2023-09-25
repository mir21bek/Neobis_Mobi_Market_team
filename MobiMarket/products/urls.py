from django.urls import path
from rest_framework import routers

from .views import ProductApiView, like_product, unlike_product, get_like_counts


router = routers.SimpleRouter()
router.register(r'api', ProductApiView)
urlpatterns = [
    path('like/', like_product, name='like-product'),
    path('unlike/<int:product_id>/', unlike_product, name='unlike-product'),
    path('like-counts/', get_like_counts, name='like-counts'),
]
urlpatterns += router.urls
