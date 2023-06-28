from django.urls import path
from .views import RegistroUsuarioView

urlpatterns = [
    path('registrate/', RegistroUsuarioView.as_view(), name='registrate'),



]