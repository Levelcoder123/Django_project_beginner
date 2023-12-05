from django.shortcuts import render

from .models import Account


def get_accounts_data(request):
    user_accounts = Account.objects.filter(user=request.user)
    context = {'user_accounts': user_accounts}

    return render(
        request, 'accounts.html', context
    )
