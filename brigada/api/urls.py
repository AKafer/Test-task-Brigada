from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CityViewSet, BrigadaViewSet, ObjectViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'brigades', BrigadaViewSet, basename='brigades')
router.register(r'objects', ObjectViewSet, basename='objects')

urlpatterns = [
    path('', include(router.urls)),
]