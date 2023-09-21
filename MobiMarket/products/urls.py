from rest_framework import routers

from .views import ProductApiView

router = routers.DefaultRouter()
router.register(r'products', ProductApiView)
urlpatterns = router.urls
