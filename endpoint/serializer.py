from django.contrib.auth.models import User, Group
from rest_framework import serializers
from endpoint.models import Coordinates


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'count')