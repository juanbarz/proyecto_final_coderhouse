from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #si borro el usuario-autor, esto va a borrar todas sus publicaciones
    cuerpo = models. TextField()
    #fecha = models.DateField()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)