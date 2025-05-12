from django.db import models
from Users.models import PetLever

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    size = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    space_required = models.TextField()
    description = models.TextField()
    compatibility = models.TextField()
    avilability = models.BooleanField(default=True)
    pet_lever = models.ForeignKey(PetLever, on_delete=models.CASCADE, related_name='pets', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
