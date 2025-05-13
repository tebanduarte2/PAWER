from django.db import models
from Users.models import PetLever
from django.utils.translation import gettext_lazy as _ 

class Pet(models.Model):
    name = models.CharField(max_length=100)
    SPECIES_CHOICES = [
        ('PERRO', _('Perro')),
        ('GATO', _('Gato')),
        ('AVE', _('Ave')),
        ('CONEJO', _('Conejo')),
        ('HAMSTER', _('Hamster')),
        ('OTRO', _('Otro')),
    ]
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    age = models.IntegerField()
    size = models.CharField(max_length=20)
    GENDER_CHOICES = [
        ('MASCULINO', _('Masculino')),
        ('FEMENINO', _('Femenino')),
        ('DESCONOCIDO', _('Desconocido')),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES) 
    space_required = models.TextField()
    description = models.TextField()
    avilability = models.BooleanField(default=True)
    pet_lever = models.ForeignKey(PetLever, on_delete=models.CASCADE, related_name='pets', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
