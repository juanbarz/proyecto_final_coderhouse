from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_tag = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #si borro el usuario-autor, esto va a borrar todas sus publicaciones
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    pais = models.CharField(max_length=30, default='N/A')
    imagen_header = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    #megusta = models.ManyToManyFIeld(User, related_name)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('home')
    
class Categoria(models.Model):
    pais = models.CharField(max_length=30, default='N/A')

    def __str__(self):
        return self.pais #si agrego otra categoria tengo que sumar + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse('home')
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    imagen_perfil = models.ImageField(null=True, blank=True, upload_to="imagenes/perfil/")
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    sitio_web = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)
    
    def get_absolute_url(self):
        return reverse('home')
    
class Comentarios(models.Model):
    articulo = models.ForeignKey(Articulo, related_name="comentario", on_delete=models.CASCADE) # si borro un articulo, se borran los comentariso
    nombre = models.CharField(max_length=155)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.articulo.titulo, self.nombre)


