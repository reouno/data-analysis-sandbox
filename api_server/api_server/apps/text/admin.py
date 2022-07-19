from django.contrib import admin

# Register your models here.
from api_server.apps.text.models import TextData

admin.site.register(TextData)