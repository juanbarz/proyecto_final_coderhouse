from django.shortcuts import render, get_object_or_404
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrateForm, EditarPerfilForm, PaginaPerfilForm
from django.views.generic import DetailView, CreateView
from tblog_app.models import Perfil

class PaginaPerfilView(DetailView):
    model = Perfil
    template_name = 'registration/perfil_usuario.html'

    def get_context_data(self, *args, **kwargs):
        #perfiles = Perfil.objects.all()
        context = super(PaginaPerfilView, self).get_context_data(*args, **kwargs)
        pagina_usuario = get_object_or_404(Perfil, id=self.kwargs['pk'])

        context["pagina_usuario"] = pagina_usuario
        return context  

class RegistroUsuarioView(generic.CreateView):
    form_class = RegistrateForm
    template_name = 'registration/registrate.html'
    success_url = reverse_lazy('login')

class EditarUsuarioView(generic.UpdateView):
    form_class = EditarPerfilForm
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class PaginaEditarPerfilView(generic.UpdateView):
    model = Perfil
    template_name = 'registration/pagina_editar_perfil.html'
    success_url = reverse_lazy('home')
    fields = ['bio', 'imagen_perfil', 'sitio_web', 'facebook', 'instagram']

class CrearPefilView(CreateView): 
    model = Perfil
    form_class = PaginaPerfilForm
    template_name = "registration/crear_perfil.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) #id usuario disponible para el id perfil


