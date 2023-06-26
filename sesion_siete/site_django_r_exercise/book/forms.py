# importar la librería estándar de Django Forms
from django import forms

# Creación de un forms
#Creación form (Rebound Exercise, sesión 7)
class InputForm(forms.Form):
    titulo = forms.CharField(max_length = 150)
    autor = forms.CharField(max_length = 150)
    valoracion = forms.IntegerField(min_value=0, max_value=10000)