from django import forms
from .models import Compra

class CompraCreateForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['usuario', 'direccion', 'lugar', 'telefono', 'total',]