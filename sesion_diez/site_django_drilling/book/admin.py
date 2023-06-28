from django.contrib import admin

# Register your models here.
from .models import BookModel
#Creación class BookAdmin para mostrar en sitio de Admin(Drilling, sesión 10)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion')
    list_filter = ('valoracion', 'modificado')
admin.site.register(BookModel, BookAdmin)
