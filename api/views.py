from rest_framework.generics import ListAPIView

from banks.models import Bank
from api.serializers import BanksSerializer


class BankListAPIView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BanksSerializer

