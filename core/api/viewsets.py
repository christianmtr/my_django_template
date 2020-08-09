from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from core.api.serializers import OrganizationSerializer, UserSerializer, UserDetailedSerializer
from core.models import Organization, User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class OrganizationViewSets(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'forgot_password']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return UserDetailedSerializer
        return UserSerializer
