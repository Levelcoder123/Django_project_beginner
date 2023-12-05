from django.shortcuts import render
from django.views import View

from .models import Bank


class BankView(View):
    def get(self, request):
        context = {'banks_data': Bank.objects.all()}

        return render(request, 'banks.html', context)
