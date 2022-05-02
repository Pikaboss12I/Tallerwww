from django.shortcuts import  render,redirect
from .models import Plato,Alimento
from .forms import PlatoForm,AlimentoForm

# Create your views here.

def home(request):
    return render(request, "Restaurante.html")

def gestionarplatos(request):
    platos = Plato.objects.all()
    form = PlatoForm()
    if request.POST:
        if request.method =='POST':
            form = PlatoForm(request.POST)
            if form.is_valid():
                form.save()
    context = {
        "platos":platos,
        'form':form
    }
    return render(request,"gestionarplatos.html",context)

def gestionaralimentos(request):
    alimentos = Alimento.objects.all()
    form = AlimentoForm()
    if request.POST:
        if request.method =='POST':
            form = AlimentoForm(request.POST)
            if form.is_valid():
                form.save()
    context = {
        "alimentos":alimentos,
        'form':form
    }
    return render(request,"gestionaralimentos.html",context)
    
def edicion(request,id):
    if Plato.objects.filter(pk=id).exists():
        plato = Plato.objects.get(pk=id)
        form = PlatoForm(instance=plato)
        if request.POST:
            if 'Guardar' in request.POST:
                form = PlatoForm(request.POST, instance=plato)
                if form.is_valid():
                    form.save()
                    return redirect('gestionarplatos')
        context = {
            "form" : form
        }
        return render(request,"editarplato.html",context)

def edicionalimento(request,id):
    if Alimento.objects.filter(pk=id).exists():
        alimento = Alimento.objects.get(pk=id)
        form = AlimentoForm(instance=alimento)
        if request.POST:
            if 'Guardar' in request.POST:
                form = AlimentoForm(request.POST, instance=alimento)
                if form.is_valid():
                    form.save()
                    return redirect('gestionaralimentos')
        context = {
            "form" : form
        }
        return render(request,"editaralimento.html",context)

def borradoalimento(request,id):
    if Alimento.objects.filter(pk=id).exists():
        alimentos = Alimento.objects.get(pk=id)
        if request.method =='POST':
            if 'Borrar' in request.POST:
                alimentos.delete()
                return redirect('gestionaralimentos')
        context = {
            "alimentos":alimentos
        }
        return render(request,"borraralimento.html",context)

def borrado(request,id):
    if Plato.objects.filter(pk=id).exists():
        plato = Plato.objects.get(pk=id)
        if request.POST:
            if 'Borrar' in request.POST:
                plato.delete()
                return redirect('gestionarplatos')
        context = {
            "plato":plato
        }
        return render(request,"borrarplato.html",context)