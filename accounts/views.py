from django.shortcuts import render
from django.views import View

# Create your views here.
from .models import Account


# Create your views here.
class AccountView(View):
    def get(self, request):
        context = {'accounts_data': Account.objects.all()}

        return render(
            request, 'accounts.html', context
        )
