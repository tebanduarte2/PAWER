from django.contrib import admin
from .models import Pet
 
# Register your models here.

class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "species") 
admin.site.register(Pet, PetAdmin)  # Registra tu modelo con la clase de administración

