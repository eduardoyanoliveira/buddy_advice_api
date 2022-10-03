from rest_framework.routers import DefaultRouter
from comments.views import CommentViewSet

app_name = 'comments'

router = DefaultRouter()

router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls