from django.urls import path
from . import views

app_name = 'space_objects'

urlpatterns = [
    path('', views.index, name='index'),
    path('cities', views.city, name='cities'),
    path('brigades/<str:city>/', views.brigada, name='brigades'),
    path('objects/<str:brigada>/', views.object, name='objects'),
]