from django.urls import path
from .views import product_list
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("products/", product_list),
]
urlpatterns = router.urls