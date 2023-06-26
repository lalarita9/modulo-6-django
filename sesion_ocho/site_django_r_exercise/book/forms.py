from django import forms
# Agregando para el uso de models
from .models import BookModel
# Agregando para el registro de usuarios 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
#Create your forms here.

class BookForm(forms.ModelForm): 
    #Especifica el nombre del modelo a usar
    class Meta: 
        model = BookModel 
        fields = "__all__" #para que se puedan usar todos
        #exclude = ['direccion'] #En caso de excluir uno

# Clase para el registro de usuarios 
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    # Especifica el nombre del modelo a usar
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user