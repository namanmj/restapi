from rest_framework import serializers

from .models import Building,Society,Flat
class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','flat_no')
class BuildingSerializer(serializers.ModelSerializer):
    flat=FlatSerializer(many=True,read_only=True)

    class Meta:
        model = Building
        fields = ('id','name','flat')

class SocietySerializer(serializers.ModelSerializer):
    building=BuildingSerializer(many=True)
    class Meta:
        model = Society
        fields = ('id','name','building')

   


    def create(self, validated_data):
        building= validated_data['building']
        
        del validated_data['building']
        society= Society.objects.create(**validated_data)

        for building in building:
            buil=Building.objects.create(**building)
            society.building.add(buil)

        society.save()
        return society
            

"""def create(self, validated_data):   
        building_data = validated_data.pop('building')
        society = Society.objects.create(**validated_data)
        Building.objects.create(society=society, **building_data)
        return society"""