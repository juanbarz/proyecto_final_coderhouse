from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Articulo

class HomeView(ListView):
    model = Articulo
    template_name = 'home.html'


class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'articulo_detalle.html'


class AgregarArticuloView(CreateView):
    model = Articulo
    template_name = 'agregar_articulo.html'
    fields = '__all__'

