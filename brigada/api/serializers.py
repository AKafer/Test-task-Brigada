from rest_framework import serializers
from objects.models import City, Brigada, Object

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class BrigadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brigada
        fields = "__all__"

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"