
from django.contrib import admin

from wallet.models import Wallet, Transaction, Transfer


class TransferInline(admin.TabularInline):
    model = Transfer


@admin.register(Wallet)
class WalletModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    inlines = (TransferInline, )
