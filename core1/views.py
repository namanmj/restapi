from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
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

class societyView(GenericAPIView):
    serializer_class = SocietySerializer
    def get(self,request):
        self.queryset = Society.objects.all()
        seriliser_obj = self.serializer_class(self.queryset,many=True)
        return Response(seriliser_obj.data)

    def post(self,request):
        data = request.data
        print(type(data))
        society_obj = Society.objects.create(name=data["name"])
        society_obj.save()
        for i in data["building"]:
            building_obj = Building.objects.create(society=society_obj,name=i["name"])
            building_obj.save()
            print(i)
            for j in i["flat"]:
                flat_obj = Flat.objects.create(society=society_obj,building=building_obj,flat_no=j["flat_no"])
                flat_obj.save()
        
        return Response({"society_id":society_obj.id})