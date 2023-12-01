from django.shortcuts import render

# Create your views here.
from .models import Account


# Create your views here.
def get_accounts(request):

    accounts_data = Account.objects.all()

    return render(
        request, 'accounts.html', {
            'accounts': accounts_data
        }
    )
