from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BrigadaViewSet, CityViewSet, ObjectViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'brigades', BrigadaViewSet, basename='brigades')
router.register(r'objects', ObjectViewSet, basename='objects')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
