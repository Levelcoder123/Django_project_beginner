from django.views.generic import ListView

from .models import Account


class AccountView(ListView):
    model = Account
    template_name = 'accounts.html'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
