from importlib.metadata import files
from operator import mod
from rest_framework import serializers
from .models import Alimento, Plato

class serial(serializers.ModelSerializer):
    class Meta:
        model=Alimento
        fields=['id','nombre','categoria']

class serial2(serializers.ModelSerializer):
    class Meta:
        model=Plato
        fields=['id','nombre','tiempo_preparacion','categoria','alimento']