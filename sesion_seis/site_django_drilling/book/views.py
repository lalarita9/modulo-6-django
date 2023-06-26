from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

#Se genera clase del tipo "TemplateView" (Drilling, sesión 4)
class IndexPageView(TemplateView):
    template_name = 'index.html'

#Creación de un método HttpResponse (Rebound Exercise, sesión 4)
def book(request):
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")

#Se crea función para verificar sí una frase o palabra es palindromo (Rebound Exercises, sesión 5)
def palindromo(request, frase):
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

#Creación del método navbar(Drilling, sesión 5)
def navbar(request):
    context = {}
    return render(request, 'navbar.html', context)

#Creación del método listbook(Rebound Exercise, sesión 6)
def listbook(request):
    #Se genera un diccionario
    libro1 = {'titulo': 'Django 3 Web Development Coobook Fourth Edition', 'autor': 'Aidas Bendoraitis', 'valoracion': 3250}      
    libro2 = {'titulo': 'Two Scoops of Django 3x', 'autor': 'Daniel Feldroy', 'valoracion': 1570}
    libro3 = {'titulo': 'El Libro de Django', 'autor': 'Adrian Holovaty', 'valoracion': 1100}
    libro4 = {'titulo': 'Python Web Development with Django', 'autor': 'Jeff Forcier', "valoracion": 1350}
    libro5 = {'titulo': 'Django for Professionals', 'autor': 'William S. Vicent',  'valoracion': 2100}
    libro6 = {'titulo': 'Django for APIs', 'autor': 'Willim S. Vicent',  'valoracion': 2540}
    libro = (libro1, libro2, libro3, libro4, libro5, libro6)     
    #Se agrega context
    context = {
        'libros': libro,
             
    }
    return render(request, 'listbook.html', context)

#Creación del método footer(Drilling, sesión 6)
def footer(request):
    context = {}
    return render(request, 'footer.html', context)