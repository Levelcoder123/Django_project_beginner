from rest_framework import serializers

from banks.models import Bank
from users.models import User


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'])

        return user
