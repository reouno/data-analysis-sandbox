from rest_framework.serializers import ModelSerializer

from api_server.apps.custom_accounts.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    """CustomUser serializer"""

    class Meta:
        """Meta"""
        model = CustomUser
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    """User profile serializer"""

    class Meta:
        """Meta"""
        model = CustomUser
        exclude = ('password',)
