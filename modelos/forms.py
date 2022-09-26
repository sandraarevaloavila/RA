from .models import *
from django.forms import ModelForm
from django import forms

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

