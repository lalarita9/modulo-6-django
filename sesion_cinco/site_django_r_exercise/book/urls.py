#Se crea el archivo urls.py para configurar las vistas de app book (Drilling, sesión 4)
#Importación de "path"
from django.urls import path
#Importación de las vistas
from .views import IndexPageView, book, palindromo


urlpatterns = [
   #Se agrega la url "index", (Drilling, sesión 4)
   path('', IndexPageView.as_view(), name = 'index'),
   #Se indica la vista book (Rebound Exercises, sesión 4)
   path('book/', book, name= 'book'),
   #Se agrega la url "palindromo", la cual debe ir acompañada
   #de una palabra o frase(Rebound Exercises, sesión 5)
   path('palindromo/<frase>', palindromo, name = 'palindromo'),

]
