from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import CustomUser


class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_filter = ('username', 'id')
    list_display = ('username', 'email')


admin.site.register(CustomUser, UserAdmin)
