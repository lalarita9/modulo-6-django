from django.db import models

# Create your models here.
class BookModel(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField()
    #Agregando dos atributos(Rebound Exercise, sesión 10)
    creado= models.DateTimeField(auto_now_add=True)
    modificado= models.DateTimeField(auto_now=True)

    #Se crea Class Meta para creación de permisos(Rebound Exercise, sesión 9)
    class Meta:
        #Configuración "verbose_name" para cambiar de Book a Libro(singular), y Libros (Plural)(Rebound Exercise, sesión 10)
        verbose_name = "libro"
        verbose_name_plural = "libros"
        
        permissions = (
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Ower"),
        )
    def __str__(self):
        return self.titulo