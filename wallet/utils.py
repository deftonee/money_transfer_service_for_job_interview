from rest_framework.exceptions import ValidationError

from wallet.models import Wallet, AssetTypeEnum


def create_wallet(user, asset, balance):
    try:
        AssetTypeEnum(asset)
    except ValueError:
        raise ValidationError(f'There is no asset with {asset} symbol')

    wallet = Wallet.objects.create(
        user=user,
        asset=asset,
        balance=balance,
    )
    return wallet
