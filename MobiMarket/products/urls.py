from django.urls import path

from .views import ProductApiView, like_product, unlike_product, get_like_counts

urlpatterns = [
    path('', ProductApiView.as_view({'get': 'list'})),
    path('like/', like_product, name='like-product'),
    path('unlike/<int:product_id>/', unlike_product, name='unlike-product'),
    path('like-counts/', get_like_counts, name='like-counts'),
]
