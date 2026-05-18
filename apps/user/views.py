from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.models import User
from apps.user.serializers import RegisterSerializer, ProfileSerializer, LoginSerializer

class RegisterAPI(mixins.CreateModelMixin,
                    GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProfileAPI(mixins.RetrieveModelMixin,
                GenericViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class LoginAPI(TokenObtainPairView):
    serializer_class = LoginSerializer  


class LogoutAPI(APIView):
    def post(self, request):
        return Response({"message": "Вы успешно вышли."}, status=status.HTTP_200_OK)

class PasswordResetRequestAPI(APIView):
    def post(self, request):
        return Response({"message": "Запрос на сброс пароля принят."}, status=status.HTTP_200_OK)

# Create your views here.
