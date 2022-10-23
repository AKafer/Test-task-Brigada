from objects.models import City, Brigada, Object
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CitySerializer, BrigadaSerializer, ObjectSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class BrigadaViewSet(viewsets.ModelViewSet):
    queryset = Brigada.objects.all()
    serializer_class = BrigadaSerializer

    @action(methods=['get'], detail=False, url_path=r'from_city/(?P<pk>\d+)')
    def load_shop_list(self, request, pk=None):
        city = get_object_or_404(City, id=pk)
        brigades = Brigada.objects.filter(city=city)
        serializer = BrigadaSerializer(brigades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    @action(methods=['get'], detail=False, url_path=r'from_brigada/(?P<pk>\d+)')
    def load_shop_list(self, request, pk=None):
        brigada = get_object_or_404(Brigada, id=pk)
        objects = Object.objects.filter(brigada=brigada)
        serializer = ObjectSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
