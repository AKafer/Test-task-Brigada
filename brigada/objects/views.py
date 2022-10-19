from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import City, Brigada, Object


def city(request):
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request, 'index.html', context)

def brigada(request, city):
    city = get_object_or_404(City, name=city)
    brigades = Brigada.objects.filter(city=city)
    context = {
        'brigades': brigades,
        'city': city
    }
    return render(request, 'brigades.html', context)

def object(request, brigada):
    brigada = get_object_or_404(Brigada, name=brigada)
    objects = Object.objects.filter(brigada=brigada)
    context = {
        'objects': objects,
        'brigada': brigada
    }
    return render(request, 'object.html', context)
