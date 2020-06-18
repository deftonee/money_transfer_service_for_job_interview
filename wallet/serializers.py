from django.conf import settings
from rest_framework import serializers


class TransferRequestSerializer(serializers.Serializer):
    transfer_to_user_with_email = serializers.EmailField()
    amount = serializers.DecimalField(
        decimal_places=settings.BALANCE_DECIMAL_PLACES,
        max_digits=settings.BALANCE_MAX_DIGITS,
    )
