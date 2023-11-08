from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_general_user', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    list_editable = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (None, {'fields': ('first_name', 'last_name')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_general_user', 'is_other_role')}),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (None, {'fields': ('first_name', 'last_name')}),
        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin', 'is_general_user', 'is_other_role')}),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
