from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import viewsets

from .serializers import BuildingSerializer,SocietySerializer
from .models import Building,Society,Flat


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SocietyViewSet(viewsets.ModelViewSet):
    queryset= Society.objects.all()
    serializer_class = SocietySerializer

class societyView(GenericAPIView):
    serializer_class = SocietySerializer
    def get(self,request):
        self.queryset= Society.objects.all()
        seriliser_obj = self.serializer_class(self.queryset,many=True)
        return Response(seriliser_obj.data)

    def post(self,request):
        data = request.data
        print(type(data))
        society_obj = Society.objects.create(name=data["name"])
        for i in data["building"]:
            building_obj = Building.objects.create(name=i["name"])
            society_obj.building.add(building_obj)
            for j in i["flat"]:
                flat_obj = Flat.objects.create(flat_no=j["flat_no"])
                flat_obj.save()
                building_obj.flat.add(flat_obj)
            building_obj.save()
        
        return Response({"society_id":society_obj.id})
    
