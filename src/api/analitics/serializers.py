from rest_framework import serializers

from accounts.models import User


class AnaliticsQuerySerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()


class LastRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'last_request',
        )
