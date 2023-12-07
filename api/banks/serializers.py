from rest_framework import serializers

from banks.models import Bank


class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
