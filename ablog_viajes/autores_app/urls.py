from django.urls import path
from .views import RegistroUsuarioView, EditarUsuarioView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrate/', RegistroUsuarioView.as_view(), name='registrate'),
    path('editar_perfil/', EditarUsuarioView.as_view(), name='editar_perfil'),
    path('autores_app/password/', auth_views.PasswordChangeView.as_view(template_name='registration/cambiar_contraseña.html')),



]