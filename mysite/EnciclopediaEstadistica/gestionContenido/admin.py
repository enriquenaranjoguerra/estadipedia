from django.contrib import admin
from gestionContenido.models import Rama, Hoja


class HojasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "formula")
    search_fields = ("nombre", "descripcion")
    list_filter = ("nombre",)


class RamasAdmin(admin.ModelAdmin):
    list_filter = ("rama",)

admin.site.register(Rama, RamasAdmin)
admin.site.register(Hoja, HojasAdmin)
