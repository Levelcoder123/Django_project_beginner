from django.shortcuts import render

from .models import Account


def get_accounts_data(request):
    context = {'user_accounts': Account.objects.filter(user=request.user)}

    return render(request, 'accounts.html', context)
