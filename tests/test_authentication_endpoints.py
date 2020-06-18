import pytest


@pytest.mark.django_db
@pytest.mark.urls('authentication.urls')
def test_registration(client):
    resp = client.post(
        '/registration',
        {
            "balance": 500,
            "asset": "RUB",
            "email": "aa1111112@aa.ru",
            "password": "12345"
        }
    )
    assert resp.status_code == 200


@pytest.mark.django_db
@pytest.mark.urls('authentication.urls')
def test_login(client, user_one):
    resp = client.post(
        '/login',
        {
            "email": user_one.email,
            "password": "1"
        }
    )
    assert resp.status_code == 200
