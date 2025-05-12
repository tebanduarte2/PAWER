from django.contrib import admin
from .models import PetLever
 
# Register your models here.

class PetLoverAdmin(admin.ModelAdmin):
    list_display = ("name", "cellphone") 
admin.site.register(PetLever, PetLoverAdmin)  # Registra tu modelo con la clase de administración
