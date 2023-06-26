from django.db import models

# Create your models here.
class BookModel(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    valoracion = models.IntegerField()

    #Se crea Class Meta para creación de permisos(Rebound Exercise, sesión 9)
    class Meta:
        permissions = (
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Ower"),
        )
    def __str__(self):
        return self.titulo