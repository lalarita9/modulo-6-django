from django.contrib import admin

# Register your models here.
from .models import BookModel
#Creación class BookAdmin para mostrar en sitio de Admin(Drilling, sesión 10)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'autor', 'valoracion', 'rating')
    list_filter = ('valoracion', 'modificado')
    
    #Creación de campo dinámico rating(Reboun Exercises, sesión 11)
    def rating(self, obj):
        if obj.valoracion > 2500:
            return "Alto" 
        if obj.valoracion >= 1000 and obj.valoracion <= 2500:
            return "Media"
        else: 
            return "Baja"
            
admin.site.register(BookModel, BookAdmin)
