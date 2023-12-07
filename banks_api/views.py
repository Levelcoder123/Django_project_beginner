from rest_framework.response import Response
from rest_framework.decorators import api_view

from banks.models import Bank
from .serializers import BankSerializer


@api_view(['GET'])
def bank_api_view(request):
    bank_data = Bank.objects.all()
    serializer = BankSerializer(bank_data, many=True)
    return Response(serializer.data)
