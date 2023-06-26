from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
#Se genera clase del tipo "TemplateView" (Drilling, sesión 4)
class IndexPageView(TemplateView):
    template_name = 'index.html'
#Creación método HttResponse (Rebound Exercise, sesión 4)
def book(request):
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")