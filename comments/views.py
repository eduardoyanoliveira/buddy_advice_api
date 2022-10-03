from rest_framework.viewsets import ModelViewSet
from comments.serializers import CommentSerializer
from comments.models import CommentModel


class CommentViewSet(ModelViewSet):
    
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
