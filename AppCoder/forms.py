from django import forms
from AppCoder.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioFormulario(forms.Form):
    nombre= forms.CharField()
    email= forms.CharField()
    contraseña= forms.CharField()

class UserRegisterForm(forms.Form):
    nombre= forms.CharField()
    email= forms.CharField()
    contraseña= forms.CharField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
