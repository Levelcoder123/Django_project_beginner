from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_filter = ('type', 'number')
    list_display = ('type', 'amount')
