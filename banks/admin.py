from django.contrib import admin

from .models import Bank


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_filter = ('name', 'is_islamic')
    list_display = ('name', 'branch')


admin.site.register(Bank, BankAdmin)
