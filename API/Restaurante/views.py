from operator import truediv
from django.shortcuts import render
from django.http import JsonResponse   

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import serial
from .serializers import serial2 
from Restaurante.models import Alimento
from Restaurante.models import Plato
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

# ------------------- ALIMENTOS ------------------------------

@api_view(['GET'])
def Ali(request):
    Alimentos = Alimento.objects.all()
    serializers = serial(Alimentos, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def AliDetail(request, pk):
    Alimentos = Alimento.objects.get(id=pk)
    serializers = serial(Alimentos, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def AliCreate(request):
    serializers = serial(data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data) 

@api_view(['POST'])
def Alieditar(request,pk):
    Alimentos = Alimento.objects.get(id=pk)
    serializers = serial(instance=Alimentos, data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data) 

@api_view(['DELETE'])
def AliBorrar(request, pk):
    Alimentos = Alimento.objects.get(id=pk)
    Alimentos.delete()
    return Response("Alimento borrado") 

#----------------- FIN ALIMENTOS ---------------------------------------
#----------------- PLATOS ----------------------------------------------

@api_view(['GET'])
def ListaPlatos(request):
    Platos = Plato.objects.all()
    serializers = serial2(Platos, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def PlatosDetail(request, pk):
    Platos = Plato.objects.get(id=pk)
    serializers = serial2(Platos, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def crearPlatos(request):
    serializers = serial2(data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data) 

@api_view(['POST'])
def PlatoEditar(request,pk):
    Platos = Plato.objects.get(id=pk)
    serializers = serial2(instance=Platos, data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data) 

@api_view(['DELETE'])
def PlatosBorrar(request, pk):
    Platos = Plato.objects.get(id=pk)
    Platos.delete()
    return Response("Alimento borrado") 