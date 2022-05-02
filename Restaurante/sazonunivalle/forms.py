from .views import Plato,Alimento
#from django import forms
from django.forms import ModelForm

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'

class AlimentoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'
