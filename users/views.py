from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
     
