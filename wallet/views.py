from decimal import Decimal

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from wallet.serializers import TransferRequestSerializer
from wallet.utils import transfer_money, get_wallet_by_email, get_operations, \
    update_rates


class TransferAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request_serializer = TransferRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        to_wallet = get_wallet_by_email(
            request_serializer.data['transfer_to_user_with_email']
        )
        from_wallet = request.user.wallet

        transfer_money(
            from_wallet,
            to_wallet,
            Decimal(request_serializer.data['amount']),
        )
        return Response()


class OperationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        operations = get_operations(request.user.wallet)
        return Response(operations)


class UpdateRatesAPIView(APIView):

    def get(self, request):
        update_rates()
        return Response()
