from rest_framework import viewsets
from endpoint.models import Coordinates
from .serializer import CoordinateSerializer
# Create your views here.


class CoordinateViewSet(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializer

    def get_queryset(self):
        queryset = Coordinates.objects.all()
        boundbox = self.request.query_params.get('bbox', None)
        if boundbox is not None:
            boundbox = boundbox.split(',')
            queryset = queryset.filter( longitude__gte=boundbox[0], latitude__gte=boundbox[1], longitude__lte=boundbox[2], latitude__lte=boundbox[3])

        return queryset
