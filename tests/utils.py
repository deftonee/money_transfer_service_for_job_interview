from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from wallet.models import Wallet, Rate


def create_user_with_wallet(email, balance, asset):
    user = User.objects.create(
        email=email,
        username=email,
        password=make_password('1'),
    )
    Wallet.objects.create(
        user=user,
        balance=balance,
        asset=asset
    )
    return user


def add_rate(asset, quote, rate):
    return Rate.objects.create(
        asset=asset,
        quote=quote,
        rate=rate,
    )


def get_balance_by_user(user):
    return User.objects.values_list(
        'wallet__balance',
        flat=True,
    ).get(
        email=user.email,
    )
