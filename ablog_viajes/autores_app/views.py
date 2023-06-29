from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import RegistrateForm, EditarPerfilForm

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

