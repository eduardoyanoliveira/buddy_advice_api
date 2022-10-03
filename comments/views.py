from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from comments.serializers import CommentSerializer
from comments.models import CommentModel
from products.models import ProductModel

class CommentViewSet(ModelViewSet):
    
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    
    @action(detail=True, methods=['GET'])
    def get_comments_by_product(self, request, pk=None):
        
        try:
            product = ProductModel.objects.get(id=pk)
        except:
            return Response({"msg": 'This product does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            comments = CommentModel.objects.filter(product=product.id)
            
            serialized_comments = CommentSerializer(comments, many=True)
            return Response( serialized_comments.data, status=status.HTTP_200_OK)
        except:
            return Response({"msg": 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
