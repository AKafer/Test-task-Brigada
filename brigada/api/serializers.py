from rest_framework import serializers

from objects.models import City, Brigada, Object

class CitySerializer(serializers.ModelSerializer):
    """Класс сериализатора тэгов."""
    class Meta:
        model = City
        fields = "__all__"

class BrigadaSerializer(serializers.ModelSerializer):
    """Класс сериализатора тэгов."""
    class Meta:
        model = Brigada
        fields = "__all__"

class ObjectSerializer(serializers.ModelSerializer):
    """Класс сериализатора тэгов."""
    class Meta:
        model = Object
        fields = "__all__"