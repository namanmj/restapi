from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BuildingSerializer,SocietySerializer
from .models import Building,Society


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SocietyViewSet(viewsets.ModelViewSet):
    queryset= Society.objects.all()
    serializer_class = SocietySerializer
    
