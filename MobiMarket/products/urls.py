from django.urls import path
from rest_framework import routers

from .views import ProductApiView, LikeApiView

router = routers.DefaultRouter()
router.register(r'', ProductApiView)
urlpatterns = ([
    path('like/<int:pk>/', LikeApiView.as_view())
] + router.urls)
