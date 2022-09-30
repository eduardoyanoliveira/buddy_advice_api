from rest_framework import viewsets, status
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    

    def get_permissions(self):
        try:
            if self.action in ['create']:
                return [AllowAny()]
            
            return [IsAuthenticated()]
        except:
            return Response({'msg': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

