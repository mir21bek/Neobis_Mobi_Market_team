from rest_framework import routers

from .views import ProductApiView

router = routers.DefaultRouter()
router.register(r'api/products', ProductApiView)
urlpatterns = router.urls
