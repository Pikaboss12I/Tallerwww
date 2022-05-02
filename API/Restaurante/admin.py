from django.contrib import admin

from Restaurante.models import Alimento, Plato

# Register your models here.
admin.site.register(Plato)
admin.site.register(Alimento)