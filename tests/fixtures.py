import pytest

from decimal import Decimal

from wallet.models import AssetTypeEnum

from tests.utils import create_user_with_wallet, add_rate


@pytest.fixture()
def user_one(db):
    return create_user_with_wallet(
        'user_one@example.com',
        100,
        AssetTypeEnum.USD.value,
    )


@pytest.fixture()
def user_two(db):
    return create_user_with_wallet(
        'user_two@example.com',
        4000,
        AssetTypeEnum.RUB.value,
    )


@pytest.fixture()
def usd_to_rub_rate(db):
    return add_rate(
        AssetTypeEnum.USD.value,
        AssetTypeEnum.RUB.value,
        70,
    )


@pytest.fixture()
def rub_to_usd_rate(db):
    return add_rate(
        AssetTypeEnum.RUB.value,
        AssetTypeEnum.USD.value,
        Decimal("0.015"),
    )
