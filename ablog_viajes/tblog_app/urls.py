from django.urls import path
from .views import HomeView, ArticuloDetailView, AgregarArticuloView, EditarArticuloView, EliminarArticuloView, AgregarCategoriaView, PaisView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('articulo/<int:pk>', ArticuloDetailView.as_view(), name='articulo-detalle'), #cada publicacion tiene un id (primarykey) el primer post sera --> publicacion/1 y asi... 
    path('agregar_articulo/', AgregarArticuloView.as_view(), name='agregar_articulo'),
    path('agregar_pais/', AgregarCategoriaView.as_view(), name='agregar_pais'),
    path('articulo/editar/<int:pk>', EditarArticuloView.as_view(), name='editar_articulo'),
    path('articulo/eliminar/<int:pk>', EliminarArticuloView.as_view(), name='eliminar_articulo'),
    path('categoria/<str:paisx>/', PaisView, name='categoria'),
]

