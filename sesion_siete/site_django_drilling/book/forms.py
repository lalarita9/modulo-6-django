# importar la librería estándar de Django Forms
from django import forms
from .models import BookModel
#Create your forms here.

#Creación ModelForm (Drilling, sesión 7)
class BookForm(forms.ModelForm): 
    #Especifica el nombre del modelo a usar
    class Meta: 
        model = BookModel 
        fields = "__all__" #para que se puedan usar todos
        #exclude = ['direccion'] #En caso de excluir uno