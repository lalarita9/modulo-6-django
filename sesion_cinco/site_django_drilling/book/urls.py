from django.urls import path
from .views import IndexPageView, book, palindromo, navbar


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

]
