from django.urls import path
from .views import HomeView, PublicacionDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('publicacion/<int:pk>', PublicacionDetailView.as_view(), name='publicacion-detalle'), #cada publicacion tiene un id (primarykey) el primer post sera --> publicacion/1 y asi... 

]