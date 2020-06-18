from django.urls import path

from wallet.views import TransferAPIView, OperationsAPIView, UpdateRatesAPIView

urlpatterns = [
    path('transfer', TransferAPIView.as_view()),
    path('operations', OperationsAPIView.as_view()),
    path('update_rates', UpdateRatesAPIView.as_view()),
]
