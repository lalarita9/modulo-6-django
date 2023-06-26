#Se crea el archivo urls.py para configurar las vistas de app book (Drilling, sesión 4)
#Importación de "path"
from django.urls import path
#Importación de las vistas
from .views import IndexPageView, book, palindromo, navbar, listbook, footer


urlpatterns = [
   #Se agrega la url "index", (Drilling, sesión 4)
   path('', IndexPageView.as_view(), name = 'index'),
   #Se indica vista book (Rebound Exercises, sesión 4)
   path('book/', book, name= 'book'),
   #Se agrega la url "palindromo", la cual debe ir acompañada
   #de una palabra o frase(Rebound Exercises, sesión 5)
   path('palindromo/<frase>', palindromo, name = 'palindromo'),
   #Se agrega la url "navbar"(Drilling, sesión 5)
   path('navbar/', navbar, name= 'navbar'),
   #Se agrega la url "listbook"(Rebound Exercises, sesión 6)
   path('listbook/', listbook, name= 'listbook'),
   #Se agrega la url "footer"(Drilling, sesión 6)
   path('footer/', footer, name= 'footer'),

]
