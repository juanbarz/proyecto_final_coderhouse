from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from tblog_app.models import Perfil

class RegistrateForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}), label="Correo electrónico")
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nombre")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Apellido")


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
        'username': 'Nombre de usuario',
        'password1': 'Contraseña',
        'password2': 'Confirmar contraseña', #revisar porque no printea bien
        }


    def __init__(self, *args, **kwargs):
        super(RegistrateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}), label="Correo electrónico")
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nombre")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Apellido")
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nombre de Usuario")
    #last_login = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email') #, 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class PaginaPerfilForm(forms.ModelForm):
    class Meta: 
        model = Perfil
        fields = ('bio', 'imagen_perfil', 'facebook', 'instagram', 'sitio_web')
        widgets = {
                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                #'imagen_perfil': forms.TextInput(attrs={'class': 'form-control'}),
                'facebook': forms.TextInput(attrs={'class': 'form-control'}),
                'instagram': forms.TextInput(attrs={'class': 'form-control'}),
                'sitio_web': forms.TextInput(attrs={'class': 'form-control'}),
            }
