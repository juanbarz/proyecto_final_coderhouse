from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #si borro el usuario-autor, esto va a borrar todas sus publicaciones
    cuerpo = models. TextField()
    #fecha = models.DateField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        #return reverse('articulo-detalle', args=(str(self.id)) )
        return reverse('home')