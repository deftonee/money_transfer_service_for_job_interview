# Generated by Django 3.0.7 on 2020-06-17 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('GPB', 'GPB'), ('RUB', 'RUB'), ('BTC', 'BTC')], max_length=5)),
                ('balance', models.DecimalField(decimal_places=6, max_digits=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=6, max_digits=16)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Transaction')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('GPB', 'GPB'), ('RUB', 'RUB'), ('BTC', 'BTC')], max_length=5)),
                ('quote', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD'), ('GPB', 'GPB'), ('RUB', 'RUB'), ('BTC', 'BTC')], max_length=5)),
                ('rate', models.DecimalField(decimal_places=6, max_digits=16)),
            ],
            options={
                'unique_together': {('asset', 'quote')},
            },
        ),
    ]
