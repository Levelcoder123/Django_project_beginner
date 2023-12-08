from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token

from banks.models import Bank
from api.serializers import BanksSerializer


class BankListAPIView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BanksSerializer


class RegWithToken(ListAPIView):
    Token.objects.get_or_create()
