from django.urls import path
from .views import gestionarplatos,gestionaralimentos,home,edicion,borrado,borradoalimento,edicionalimento

urlpatterns = [
    path('', home, name="home"),
    path('platos', gestionarplatos, name="gestionarplatos"),
    path('alimentos',gestionaralimentos,name="gestionaralimentos"),
    path('editar/<str:id>',edicion,name="edicion"),
    path('editarAlimento/<str:id>',edicionalimento,name="edicionalimento"),
    path('borrar/<str:id>',borrado,name="borrado"),
    path('borrarAlimento/<str:id>',borradoalimento,name="borradoalimento")
]