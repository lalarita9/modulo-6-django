
from django.http import HttpResponse

# Create your views here.
def mensaje(request):
    return HttpResponse('''<h1>Mi primer Proyecto Django</h1><br>
                        <h3>Función de los siguientes comandos:</h3>
                        <p>Makemigrations: Detecta cambios, <em>No changes detected</em></p>
                        <p>Migrate: Realiza migracion de admin, auth, contenttypes, sessions</p>
                        <p>Shell: Interacción con la consola de Python que permite realizar operaciones</p>
                        <p>Dbshell: Ejecuta línea de cliente, usuario/contraseña</p>
                        <p>Showmigrations: Muestra todas las migraciones de un proyecto, puede elegir uno
                        de los dos formatos</p>
                        <p>Dumpdata: Muestra un diccionario</p>
                        <p>Test: Ejecuta prueba para todas las aplicaciones instaladas</p>
                        <p>Testserver: Ejecuta un servidor de desarrollo de Django</p>
                        <p>Diffsetting: Muestra las diferencias entre el archivo de configuración actual 
                        y la configuración predeterminada de Django (u otro archivo de configuración 
                        especificado por --default).</p>
                        ''')
def about(request):
    return HttpResponse("about")
