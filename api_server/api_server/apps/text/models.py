from django.db import models

# Create your models here.
from api_server.apps.custom_accounts.models import CustomUser


class Lang(models.TextChoices):
    """Language code"""
    JA = 'ja'
    EN = 'en'


class AnalysisType(models.TextChoices):
    """Analysis type"""
    TOKENIZE = 'tokenize'


class TextData(models.Model):
    """Text data table"""
    user = models.ForeignKey(to=CustomUser, on_delete=models.SET_NULL, null=True)
    data = models.TextField()
    lang = models.CharField(choices=Lang.choices, max_length=2)
    analysis_type = models.CharField(choices=AnalysisType.choices, max_length=20)
    params = models.JSONField(blank=True, null=True)
    result = models.JSONField(blank=True, null=True)
