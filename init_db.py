from os import getenv

from django.contrib.auth.models import User


ADMIN_LOGIN = getenv('ADMIN_LOGIN', 'admin')
ADMIN_PASSWORD = getenv('ADMIN_PASSWORD', 'admin')
ADMIN_EMAIL = getenv('ADMIN_EMAIL', 'admin@example.com')

admin_exists = User.objects.filter(username=ADMIN_LOGIN).exists()

if not admin_exists:
    User.objects.create_superuser(
        username=ADMIN_LOGIN,
        password=ADMIN_PASSWORD,
        email=ADMIN_EMAIL,
    )
    print('Administrator account created')
else:
    print('User with specified username already exists')
