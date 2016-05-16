from rest_framework import serializers
from endpoint.models import Coordinates
#declaration of fields for serialization for api


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude', 'longitude', 'count')