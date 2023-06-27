from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publicacion

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Publicacion
    template_name = 'home.html'


class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = 'publicacion_detalle.html'

