from django.conf import settings
from rest_framework import serializers

from wallet.models import AssetTypeEnum


class RegisterRequestSerializer(serializers.Serializer):
    balance = serializers.DecimalField(
        decimal_places=settings.BALANCE_DECIMAL_PLACES,
        max_digits=settings.BALANCE_MAX_DIGITS,
    )
    asset = serializers.ChoiceField(choices=AssetTypeEnum.choices())
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
