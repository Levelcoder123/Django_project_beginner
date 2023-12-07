from rest_framework.response import Response
from rest_framework.decorators import api_view

from banks.models import Bank
from .serializers import BanksSerializer


@api_view(['GET'])
def banks_api_view(request):
    bank_data = Bank.objects.all()
    serializer = BanksSerializer(bank_data, many=True)
    return Response(serializer.data)
