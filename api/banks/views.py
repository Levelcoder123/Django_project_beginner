from rest_framework.generics import ListAPIView

from banks.models import Bank
from .serializers import BanksSerializer


class BanksApiView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BanksSerializer
