from django.urls import path
from rest_framework import routers

from .views import ProductApiView, like_product, unlike_product, get_like_counts, MyProductApiView

router = routers.SimpleRouter()
router.register(r'product/api', MyProductApiView)
urlpatterns = [
    path('all-products/', ProductApiView.as_view()),
    path('like/<int:product_id>/', like_product, name='like-product'),
    path('unlike/<int:product_id>/', unlike_product, name='unlike-product'),
    path('like-counts/<int:product_id>/', get_like_counts, name='like-counts'),
]
urlpatterns += router.urls
