from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet

app_name = 'users'

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')

urlpatterns = router.urls