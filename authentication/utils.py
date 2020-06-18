from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


def register_user(email, password):
    if User.objects.filter(email=email).exists():
        raise ValidationError('User with same email already exists')
    user = User.objects.create(
        username=email,
        email=email,
        password=make_password(password),
    )
    return user


def authenticate(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
