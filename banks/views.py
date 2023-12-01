from django.shortcuts import render

from .models import Bank


# Create your views here.
def get_banks(request):
    banks_data = Bank.objects.all()

    return render(
        request, 'banks.html', {
            'banks': banks_data,
        }
    )
