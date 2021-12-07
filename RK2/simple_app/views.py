from django.shortcuts import render
from rest_framework import viewsets

from simple_app.models import Streets, Houses
from simple_app.serializers import StreetSerializer, HouseSerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Streets.objects.all()
    serializer_class = StreetSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = Houses.objects.all()
    serializer_class = HouseSerializer


def report(request):
    return render(request, 'report.html', {'data': {
        'houses': Houses.objects.select_related('street_id')
    }})
