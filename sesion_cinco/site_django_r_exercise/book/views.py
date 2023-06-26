from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
#Se indica la vista indexPageView, (Drilling, sesión 4)
class IndexPageView(TemplateView):
    template_name = 'index.html'

#Se indica la vista book (Rebound Exercises, sesión 4)
def book(request):
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")

#Se crea función para verificar sí una frase o palabra es palíndromo (Rebound Exercises, sesión 5)
def palindromo(request, frase):
    frase = frase
    #Lo recibido(frase), se convierte a minuscula
    palabras= frase.lower()
    #Lo recibido(frase), se elimina los espacios
    palabras= frase.replace(" ", "")
    #Para verificar que lo recibido de izquierda a derecha se le igual
    reversa = palabras[::-1]
            
    context = {
        'palabras' : palabras,
        'reversa': reversa,
        'frase': frase,
    }
    return render(request, 'palindromo.html', context)

