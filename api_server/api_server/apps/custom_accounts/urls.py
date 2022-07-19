from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_server.apps.custom_accounts.views import UserViewSet, UserProfileViewSet, SetCsrf

router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', UserProfileViewSet.as_view()),
    path('set-csrf/', SetCsrf.as_view()),
]
