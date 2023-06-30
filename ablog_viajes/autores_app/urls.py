from django.urls import path
from .views import RegistroUsuarioView, EditarUsuarioView, PaginaPerfilView, PaginaEditarPerfilView, CrearPefilView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrate/', RegistroUsuarioView.as_view(), name='registrate'),
    path('editar_perfil/', EditarUsuarioView.as_view(), name='editar_perfil'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='cambiar_contraseña.html')),
    path('<int:pk>/perfil/', PaginaPerfilView.as_view(), name='pagina_perfil'),
    path('<int:pk>/pagina_editar_perfil/', PaginaEditarPerfilView.as_view(), name='pagina_editar_perfil'),
    path('crear_perfil/', CrearPefilView.as_view(), name='crear_perfil'),


]