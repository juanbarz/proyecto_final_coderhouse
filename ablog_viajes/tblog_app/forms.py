from django import forms
from .models import Articulo, Categoria, Comentarios

#paises
#choices = [('Argentina', 'Argentina'), ('Brasil', 'Brasil'), ('Chile', 'Chile'),]
choices = Categoria.objects.all().values_list('pais','pais')
lista_pais = []

for item in choices:
    lista_pais.append(item)


class ArticuloForm(forms.ModelForm):
    class Meta: #sin esto model y fields no funciona
        model = Articulo
        fields = ('titulo', 'titulo_tag', 'autor', 'pais', 'cuerpo', 'imagen_header')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '[Pais] LUGAR - Texto/copy' }), #form-control - formgroup
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'juan', 'type':'hidden'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(choices=lista_pais, attrs={'class': 'form-control', 'placeholder': 'Seleccionar' }),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditarForm(forms.ModelForm): #para que no se pueda editar el autor
    class Meta: 
        model = Articulo
        fields = ('titulo', 'titulo_tag', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LUGAR - texto/copy' }), #form-control - formgroup
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LUGAR'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AgregarComentarioForm(forms.ModelForm): 
    class Meta: 
        model = Comentarios
        fields = ('nombre', 'cuerpo')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), #form-control - formgroup
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '¿Que te pareció este artículo? ¿Que otro lugar me recomendas para viajar?'}),
        }