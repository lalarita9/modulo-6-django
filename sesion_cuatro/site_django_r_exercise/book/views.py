from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Creación método HttResponse (Rebound Exercise, sesión 4)
def index(request):
    return HttpResponse("Bienvenidos a mi sitio de libros")
#Creación método HttResponse (Rebound Exercise, sesión 4)
def book(request):
    return HttpResponse("Bienvenidos a mi sitio de libros")