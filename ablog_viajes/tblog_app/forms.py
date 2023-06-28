from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta: #sin esto model y fields no funciona
        model = Articulo
        fields = ('titulo', 'titulo_tag', 'autor', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '[PAIS] Lugar - texto/copy' }), #form-control - formgroup
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditarForm(forms.ModelForm): #para que no se pueda editar el autor
    class Meta: 
        model = Articulo
        fields = ('titulo', 'titulo_tag', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '[PAIS] Lugar - texto/copy' }), #form-control - formgroup
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lugar'}),
            #'autor': forms.Select(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
        }