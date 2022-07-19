"""Admin console configurations for Account app"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from api_server.apps.custom_accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Admin configuration for CustomUser"""
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_superuser', 'is_active', 'groups',)
    fieldsets = (
        (None, {'fields': ('uuid', 'username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('uuid',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)


admin.site.register(CustomUser, CustomUserAdmin)
