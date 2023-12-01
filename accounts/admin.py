from django.contrib import admin

from .models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_filter = ('type', 'number')
    list_display = ('type', 'amount')


admin.site.register(Account, AccountAdmin)
