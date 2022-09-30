from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet

app_name = 'products'

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')

urlpatterns = router.urls