from django import forms
from .models import Perro , Gato

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = '__all__'
class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = '__all__'
class BuscarForm(forms.Form):
    termino_de_busqueda = forms.CharField(max_length=50, label='Buscar')