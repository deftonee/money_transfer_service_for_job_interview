import pytest

from decimal import Decimal

from tests.utils import get_balance_by_user


@pytest.mark.django_db
@pytest.mark.urls('wallet.urls')
def test_update_rates(client):
    resp = client.get('/update_rates')
    assert resp.status_code == 200


@pytest.mark.django_db
@pytest.mark.urls('wallet.urls')
def test_transfer(client, user_one, user_two, usd_to_rub_rate, rub_to_usd_rate):
    client.force_login(user_one)
    resp = client.post(
        '/transfer',
        {
            "transfer_to_user_with_email": user_two.email,
            "amount": 10
        }
    )
    assert resp.status_code == 200
    assert get_balance_by_user(user_one) == 90
    assert get_balance_by_user(user_two) == 4700

    client.force_login(user_two)
    resp = client.post(
        '/transfer',
        {
            "transfer_to_user_with_email": user_one.email,
            "amount": 70
        }
    )
    assert resp.status_code == 200

    assert get_balance_by_user(user_one) == Decimal('91.05')
    assert get_balance_by_user(user_two) == 4630

    resp = client.get('/operations')

    assert resp.status_code == 200
    assert len(resp.data) == 2
    assert Decimal(resp.data[0][1]) == 700
    assert Decimal(resp.data[1][1]) == - 70
