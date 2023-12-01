from django.contrib import admin

from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_filter = ('name', 'id')
    list_display = ('name', 'email')


admin.site.register(User, UserAdmin)
