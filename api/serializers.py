from rest_framework import serializers
from . import models


class Location(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ['text', 'code']
        read_only_fields = ['hash']
