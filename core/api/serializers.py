from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from core.models import Organization, User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs['email'] = attrs['email'].lower()

        data = super().validate(attrs)

        refresh = super().get_token(self.user)

        user_serialized = UserSerializer(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = user_serialized.data

        update_last_login(None, self.user)

        return data


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailedSerializer(UserSerializer):
    organization = OrganizationSerializer()
