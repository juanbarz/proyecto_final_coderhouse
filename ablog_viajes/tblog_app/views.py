from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Articulo
from .forms import ArticuloForm, EditarForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Articulo
    template_name = 'home.html'
    ordering = ['-fecha']
    #ordering = ['-id'] #se ordena por creacion de id de abajo hacia arriba, luego modificar por fecha


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulo_detalle.html'


class AgregarArticuloView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'agregar_articulo.html'
    #fields = '__all__'


class EditarArticuloView(UpdateView):
    model = Articulo
    form_class = EditarForm
    template_name = 'editar_articulo.html'
    #fields = ['titulo', 'titulo_tag', 'cuerpo'] 


class EliminarArticuloView(DeleteView):
    model = Articulo
    template_name = 'eliminar_articulo.html'
    success_url = reverse_lazy('home')