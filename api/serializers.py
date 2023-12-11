from rest_framework import serializers

from banks.models import Bank
from users.models import User
from accounts.models import Account


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '_all_'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['number', 'type', 'amount']
