from rest_framework import serializers

from core1.models import Building,Society,Flat
class FlatSerializer(serializers.ModelSerializer):
    society=serializers.StringRelatedField()
    building=serializers.StringRelatedField()
    class Meta:
        model=Flat
        fields=('id','society','building','flat_no')

class BuildingSerializer(serializers.ModelSerializer):
    flat=FlatSerializer(many=True,read_only=True)
    society=serializers.StringRelatedField()

    class Meta:
        model = Building
        fields = ('id','society','name','flat')

class SocietySerializer(serializers.ModelSerializer):
    build=BuildingSerializer(many=True,read_only=True)
    class Meta:
        model = Society
        fields = ('id','name','build')

    

   


   