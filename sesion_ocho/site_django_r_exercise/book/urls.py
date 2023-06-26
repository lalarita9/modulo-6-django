#Se crea el archivo urls.py para configurar las vistas de app book (Drilling, sesión 4)
#Importación de "path"
from django.urls import path
#Importación de las vistas
from .views import IndexPageView, book, palindromo, navbar, footer, listbook, input_models, registro_book


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
   #Se agrega la url "inputbook"(Drilling, sesión 7)
   path('inputbook/', input_models, name= 'inputbook'),
   #Se agrega la url "registro"(Drilling, sesión 7)
   path('registro/', registro_book, name= 'registro'),
   

]