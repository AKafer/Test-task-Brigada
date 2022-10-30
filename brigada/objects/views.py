from django.shortcuts import get_object_or_404, render

from .models import Brigada, City, Object


def index(request):
    return render(request, 'index.html')


def city(request):
    cities = City.objects.all()
    brigades = Brigada.objects.all()
    objects = Object.objects.all()
    context = {
        'cities': cities,
        'brigades': brigades,
        'objects': objects,
    }
    return render(request, 'index2.html', context)


def brigada(request, city):
    """Добавить докстринги."""

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
