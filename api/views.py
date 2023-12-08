from django.contrib.auth import authenticate
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from banks.models import Bank
from api.serializers import BanksSerializer, UsersSerializer
from users.models import User


class BankListAPIView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BanksSerializer


class CreateUserTokenAPIView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'error': 'something wrong'}, status=status.HTTP_403_FORBIDDEN)

        serializer.save()

        user = User.objects.get(username=serializer.data['username'])

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid user name or password'}, status=status.HTTP_400_BAD_REQUEST)
