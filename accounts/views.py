from django.shortcuts import render
from django.views import View

from .models import Account


class AccountView(View):
    def get(self, request):
        context = {'user_accounts': Account.objects.filter(user=request.user)}

        return render(request, 'accounts.html', context)
