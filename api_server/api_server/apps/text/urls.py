"""url routing of text app"""
from django.urls import path

from api_server.apps.text.views.tokenization import TokenizationAPI

urlpatterns = [
    path('tokenize/', TokenizationAPI.as_view()),
]
