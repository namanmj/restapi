from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core1.serializers import BuildingSerializer,SocietySerializer,FlatSerializer
from core1.models import Building,Society,Flat

class FlatViewset(viewsets.ModelViewSet):
    queryset= Flat.objects.all()
    serializer_class = FlatSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SocietyViewSet(viewsets.ModelViewSet):
    queryset= Society.objects.all()
    serializer_class = SocietySerializer