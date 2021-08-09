from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django_restql.mixins import QueryArgumentsMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models


class GetChildren(QueryArgumentsMixin, ListAPIView):
    serializer_class = serializers.Location
    model = models.Location

    def get_queryset(self):
        try:
            return self.model.objects.get(code=self.kwargs.get('code')).get_children()
        except self.model.DoesNotExist:
            return None


class Details(RetrieveAPIView):
    serializer_class = serializers.Location
    lookup_field = 'code'
    queryset = models.Location.objects.all()
