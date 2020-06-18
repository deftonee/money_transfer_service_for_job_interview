from enum import Enum

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class AssetTypeEnum(Enum):
    EUR = 'EUR'
    USD = 'USD'
    GPB = 'GPB'
    RUB = 'RUB'
    BTC = 'BTC'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def assets(cls):
        return tuple(i.value for i in cls)


class Wallet(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    asset = models.CharField(choices=AssetTypeEnum.choices(), max_length=5)
    balance = models.DecimalField(
        decimal_places=settings.BALANCE_DECIMAL_PLACES,
        max_digits=settings.BALANCE_MAX_DIGITS,
    )


class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Transfer(models.Model):
    transaction = models.ForeignKey(to=Transaction, on_delete=models.CASCADE)
    wallet = models.ForeignKey(to=Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(
        decimal_places=settings.BALANCE_DECIMAL_PLACES,
        max_digits=settings.BALANCE_MAX_DIGITS,
    )


class Rate(models.Model):
    asset = models.CharField(choices=AssetTypeEnum.choices(), max_length=5)
    quote = models.CharField(choices=AssetTypeEnum.choices(), max_length=5)
    rate = models.DecimalField(
        decimal_places=settings.BALANCE_DECIMAL_PLACES,
        max_digits=settings.BALANCE_MAX_DIGITS,
    )

    class Meta:
        unique_together = ('asset', 'quote')
