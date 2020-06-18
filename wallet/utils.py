import logging
import requests

from json import JSONDecodeError
from django.conf import settings
from django.db import transaction
from rest_framework.exceptions import NotFound

from wallet.models import Wallet, AssetTypeEnum, Transaction, Transfer, Rate


logger = logging.getLogger(__name__)


def create_wallet(user, asset, balance):
    try:
        AssetTypeEnum(asset)
    except ValueError:
        raise NotFound(f'There is no asset with {asset} symbol')

    wallet = Wallet.objects.create(
        user=user,
        asset=asset,
        balance=balance,
    )
    return wallet


def get_wallet_by_email(email):
    try:
        wallet = Wallet.objects.get(user__email=email)
    except Wallet.DoesNotExist:
        raise NotFound(f'There is no data for user with email {email}')
    else:
        return wallet


@transaction.atomic()
def transfer_money(from_wallet, to_wallet, amount):
    quote_amount = get_quote_amount(from_wallet.asset, to_wallet.asset, amount)
    t = Transaction.objects.create()
    Transfer.objects.create(
        transaction=t,
        wallet=from_wallet,
        amount= - amount,
    )
    Transfer.objects.create(
        transaction=t,
        wallet=to_wallet,
        amount=quote_amount,
    )

    from_wallet.balance -= amount
    to_wallet.balance += quote_amount
    from_wallet.save(update_fields=('balance', ))
    to_wallet.save(update_fields=('balance', ))


def get_operations(wallet):
    return Transfer.objects.filter(
        wallet=wallet
    ).values_list(
        'transaction__created_at',
        'amount',
    )


def request_rates_from_exchangeratesapi(asset):
    result = {}
    try:
        response = requests.get(
            url='https://api.exchangeratesapi.io/latest',
            params={'base': asset}
        )
        if response.ok:
            result = response.json()
        else:
            response.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError, JSONDecodeError) as e:
        logger.warning(f'Unable to get rates for {asset}: {e}')
    return result


def update_rates():
    Rate.objects.all().delete()
    new_rates = []
    assets = AssetTypeEnum.assets()
    for asset in assets:
        data = request_rates_from_exchangeratesapi(asset)
        if not data:
            continue
        for quote_from_data, rate_from_data in data['rates'].items():
            if quote_from_data not in assets:
                continue
            new_rates.append(
                Rate(
                    asset=asset,
                    quote=quote_from_data,
                    rate=rate_from_data,
                )
            )
    Rate.objects.bulk_create(new_rates)


def get_quote_amount(base_asset, quote_asset, amount):
    try:
        rate = Rate.objects.values_list(
            'rate', flat=True
        ).get(
            asset=base_asset,
            quote=quote_asset,
        )
    except Rate.DoesNotExist:
        raise NotFound(
            f'Rates for {base_asset} and {quote_asset} currencies not found'
        )
    else:
        return rate * amount / settings.MULTIPLICITY
