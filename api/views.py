from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import AccountSerializer, BankSerializer
from banks.models import Bank
from users.models import User
from accounts.models import Account


class BankListAPIView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class TokenObtainAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user, created = User.objects.get_or_create(username=username)

        if not created:
            user = authenticate(username=username, password=password)
            if user is None:

                return Response({'detail': 'Invalid credentials'},
                                status=status.HTTP_401_UNAUTHORIZED)
            else:
                token = Token.objects.get(user=user)

                return Response({'token': token.key},
                                status=status.HTTP_200_OK)
        else:
            user.set_password(password)
            user.save()

            token = Token.objects.create(user=user)

            return Response({'token': token.key},
                            status=status.HTTP_200_OK)


class AccountListCreateAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class CreateBankAPIView(CreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
