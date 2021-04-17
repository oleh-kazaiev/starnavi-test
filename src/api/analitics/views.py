from rest_framework import generics

from accounts.models import User
from . import serializers
from .services.analitics_service import AnaliticsService


class AnaliticsView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query_serializer = serializers.AnaliticsQuerySerializer(data=self.request.query_params)
        query_serializer.is_valid(raise_exception=True)
        validated_data = query_serializer.validated_data
        return AnaliticsService().get_analitics(date_from=validated_data.get('date_from'), date_to=validated_data.get('date_to'))


class LastRequestView(generics.ListAPIView):
    serializer_class = serializers.LastRequestSerializer
    queryset = User.objects.all()
