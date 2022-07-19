# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_server.apps.custom_accounts.models import CustomUser
from api_server.apps.custom_accounts.serializers import CustomUserSerializer, UserProfileSerializer


class UserViewSet(ModelViewSet):
    """User view set"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserProfileViewSet(APIView):
    """Current user's profile view"""

    def get(self, _request):
        """Return current user's profile"""
        user = CustomUser.objects.get_by_natural_key(self.request.user)

        return Response(UserProfileSerializer(user).data)


class SetCsrf(APIView):
    """Set csrf token"""
    permission_classes = []

    # set csrf token before signup
    @method_decorator(ensure_csrf_cookie)
    def get(self, _request):
        """Set csrf token"""
        return Response({'message': 'CSRF token set'})
