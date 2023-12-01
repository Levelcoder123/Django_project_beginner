from django.shortcuts import render

# Create your views here.
from .models import Account


# Create your views here.
def get_accounts_data(request):
    context = {'accounts_data': Account.objects.all()}

    return render(
        request, 'accounts.html', context
    )
