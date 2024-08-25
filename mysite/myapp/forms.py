from django import forms
from .models import Emisor,Gasto

class EmisorForm(forms.ModelForm):
    class Meta:
        model = Emisor
        fields = ['dni', 'nombre', 'apellido', 'celular', 'imagen_dni1', 'imagen_dni2']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['tipo_gasto', 'monto', 'fecha', 'descripcion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }