from django.contrib import admin

from .models import Brigada, City, Object


class AdminCity(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class AdminBrigada(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'head', 'amount_people', 'qualification', 'city'
    )
    search_fields = (
        'name', 'head', 'amount_people',
        'qualification', 'city__name'
    )
    empty_value_display = '-пусто-'


admin.site.register(City, AdminCity)
admin.site.register(Brigada, AdminBrigada)
admin.site.register(Object)
