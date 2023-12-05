from django.contrib import admin

from .models import Bank


class BankAdmin(admin.ModelAdmin):
    list_filter = ('name', 'is_islamic')
    list_display = ('name', 'branch')


admin.site.register(Bank, BankAdmin)
