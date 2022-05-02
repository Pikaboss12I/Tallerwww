from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('alimentos-list/', views.Ali, name="alimentos-list"),
    path('alimentos-detail/<str:pk>', views.AliDetail, name="alimentos-detail"),
    path('alimentos-create/', views.AliCreate, name="alimentos-create"),
    path('alimentos-editar/<str:pk>', views.Alieditar, name="alimentos-editar"),
    path('alimentos-borrar/<str:pk>', views.AliBorrar, name="alimentos-borrar"),
    path('platos-list/', views.ListaPlatos, name='platos-list'),
    path('platos-detail/<str:pk>', views.ListaPlatos, name='platos-detail'),
    path('platos-create/', views.crearPlatos, name='platos-create'),
    path('platos-editar/<str:pk>', views.PlatoEditar, name='platos-editar'),
    path('platos-delete/<str:pk>', views.PlatosBorrar, name='platos-delete')
]