from .models import *
from django.forms import ModelForm
from django import forms

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields ={
                'usuario',
                'contraseña',
                'nombres' ,
                'apellidos' ,
                'email' ,
                'dirección' ,
                'lugar',
                'teléfono' ,

        }

        widgets = {
            'usuario':forms.TextInput(),
            'contraseña':forms.PasswordInput(),
            'nombres':forms.TextInput(),
            'apellidos':forms.TextInput(),
            'email':forms.TextInput(),
            'dirección':forms.TextInput(),
            'lugar':forms.TextInput(),
            'teléfono':forms.TextInput(),

        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contactenos
        fields = {
            'nombre',
            'correo',
            'tipo_consulta',
            'mensaje',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'correo': forms.TextInput(),
            'tipo_consulta': forms.Select(),
            'mensaje': forms.Textarea(),
        }
