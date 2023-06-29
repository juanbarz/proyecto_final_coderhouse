from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articulo, Categoria
from .forms import ArticuloForm, EditarForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Articulo
    template_name = 'home.html'
    ordering = ['-fecha']
    #ordering = ['-id'] #se ordena por creacion de id de abajo hacia arriba, luego modificar por fecha

    def get_context_data(self, *args, **kwargs):
        paises_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["paises_menu"] = paises_menu
        return context

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulo_detalle.html'

    def get_context_data(self, *args, **kwargs):
        paises_menu = Categoria.objects.all()
        context = super(ArticuloDetailView, self).get_context_data(*args, **kwargs)
        context["paises_menu"] = paises_menu
        return context



class AgregarArticuloView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'agregar_articulo.html'
    #fields = '__all__'

class AgregarCategoriaView(CreateView):
    model = Categoria
    template_name = 'agregar_pais.html'
    fields = '__all__'

class EditarArticuloView(UpdateView):
    model = Articulo
    form_class = EditarForm
    template_name = 'editar_articulo.html'
    #fields = ['titulo', 'titulo_tag', 'cuerpo'] 


class EliminarArticuloView(DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('home')

def PaisListaView(request):
    paises_lista = Categoria.objects.all()
    return render(request, 'paises_lista.html',{'paises_lista':paises_lista})

def PaisView(request, paisx):
    categoria_articulo = Articulo.objects.filter(pais=paisx)
    return render(request, 'paises.html',{'paisx':paisx.title(), 'categoria_articulo':categoria_articulo})
