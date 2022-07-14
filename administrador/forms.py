from tkinter import Widget
from django import forms
from .models import Servicio


class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Servicio
        fields = '__all__'

    


