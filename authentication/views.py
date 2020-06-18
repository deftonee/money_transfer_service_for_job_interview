from django.contrib.auth import login
from django.db import transaction
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import (
    RegisterRequestSerializer,
    LoginRequestSerializer,
)
from authentication.utils import register_user, authenticate
from wallet.utils import create_wallet


class RegisterAPIView(APIView):

    def post(self, request):
        request_serializer = RegisterRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            user = register_user(
                email=request_serializer.data['email'],
                password=request_serializer.data['password'],
            )
            create_wallet(
                user=user,
                asset=request_serializer.data['asset'],
                balance=request_serializer.data['balance'],
            )

        login(request, user)
        return Response()


class LoginAPIView(APIView):

    def post(self, request):
        request_serializer = LoginRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        user = authenticate(**request_serializer.data)
        if not user:
            raise PermissionDenied

        login(request, user)

        return Response()
