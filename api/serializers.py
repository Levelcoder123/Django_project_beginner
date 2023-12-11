from rest_framework import serializers

from banks.models import Bank
from users.models import User
from accounts.models import Account


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['number', 'type', 'amount']
