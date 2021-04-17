from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .services.auth_service import AuthService


class SignUpView(generics.GenericAPIView):
    serializer_class = serializers.SigUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        return AuthService().sign_up(email=validated_data.get('email'), password=validated_data.get('password'))


class SignInView(generics.GenericAPIView):
    serializer_class = serializers.SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        return AuthService().sign_in(email=validated_data.get('email'), password=validated_data.get('password'))
