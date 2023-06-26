from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import BookForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import BookModel
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


#Creación del método input_models(Drilling, sesión 7)
def input_models(request):
    context = {}
    form = BookForm(request.POST or None, request.FILES or None)
    #Sí el formulario está correcto se redirecciona a index
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request,'inputbook.html', context)

#Creación método registro_book(Rebound Exercise, sesión 8) 
def registro_book(request):
    #Primer if para verificar que el usuario no esté en la BD
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        #Segundo if para verificar que la información esté correcta
        if form.is_valid():
            #Se obtiene el content_type del módelo(Drilling, sesión 9)
            content_type = ContentType.objects.get_for_model(BookModel)
            #Se obtiene el permiso a asignar
            development = Permission.objects.get(
                codename='development',
                content_type=content_type
            )
            add_book = Permission.objects.get(
                codename='add_bookmodel',
                content_type=content_type
            )
            view_book = Permission.objets.get(
                codename='view_bookmodel',
                content_type=content_type
            )
            user = form.save()
            #Se agrega permiso al usuario
            user.user_permissions.add(development, add_book, view_book)
            user.is_staff = True
            #Sí está correcto el usuario, se usará login para que él inicié su sesión
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/navbar')
        #De lo contrario generará un mensaje error
        messages.error(request, "Registro invalido. Algunos datos son incorrectos")
    form = RegistroUsuarioForm()
    context = {"register_form" : form } 
    return render(request, "registro.html", context)

#Creación método login_book, inicio sesión de un usuario (Drilling, sesión 8)
def login_book(request):
    #Validación de Datos
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #Sí las credenciales son correctas, se inicia sesión:
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como:{username}.")
                return HttpResponseRedirect('/navbar')
            #Sí los campos son invalidos:
            else:
                messages.error(request, "Invalido username o password.")
        
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

#Creación método logout_book, cierre de Sesión del usuario (Drilling, sesión 8)
def logout_book(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente")
    return HttpResponseRedirect('/login')