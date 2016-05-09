
from django.shortcuts import render
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from endpoint.models import Coordinates
from .serializer import CoordinateSerializer
from rest_framework import filters

# Create your views here.

class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer


    def get_queryset(self):
        queryset = Coordinates.objects.all()
        maxlat = self.request.query_params.get('maxlat', None)
        minlat = self.request.query_params.get('minlat', None)
        maxlong = self.request.query_params.get('maxlong', None)
        minlong = self.request.query_params.get('minlong', None)
        if maxlat is not None and minlat is not None and maxlong is not None and minlong is not None:
            queryset = queryset.filter(lattitude__lte=maxlat, lattitude__gte=minlat, longitude__lte=maxlong, longitude__gte=minlong)

        return queryset



