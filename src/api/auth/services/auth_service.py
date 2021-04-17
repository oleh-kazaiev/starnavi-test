from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from accounts.models import User


class AuthService:
    def sign_up(self, email, password):
        user = User.objects.create_user(
            email=email,
            password=password,
            is_active=True
        )
        token = self._generate_auth_token(user)
        return Response({'token': token})

    def sign_in(self, email, password):
        user = authenticate(email=email, password=password)
        if user:
            token = self._generate_auth_token(user)
            return Response({'token': token})
        return Response({'error': 'Bad credentials'}, status=status.HTTP_400_BAD_REQUEST)

    def _generate_auth_token(self, user: User):
        return Token.objects.get_or_create(user=user)[0].key
