from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

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

# Create your views here.
