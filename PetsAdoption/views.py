from django.shortcuts import render, redirect, get_object_or_404
from django import forms 
from django.views import View
from .models import Pet
from .forms import PetForm
from rest_framework import generics
from .serializers import PetSerializer
from django.shortcuts import render

class AvailablePetsListView(generics.ListAPIView):
    queryset = Pet.objects.filter(avilability=True)
    serializer_class = PetSerializer


class PetCatalogView(View):
    def get(self, request):
        pets = Pet.objects.all()
        query = request.GET.get('q', '')
        species = request.GET.get('species', '')
        size_min = request.GET.get('size_min', '')
        size_max = request.GET.get('size_max', '')

        # Filtrado por búsqueda
        if query:
            pets = pets.filter(name__icontains=query) | pets.filter(description__icontains=query)

        # Filtrado por especie
        if species:
            pets = pets.filter(species=species)

        # Filtrado por rango de tamaño
        if size_min:
            pets = pets.filter(size__gte=size_min)
            
        if size_max:
            pets = pets.filter(size__lte=size_max)

        return render(request, 'catalog.html', {'pets': pets})
    
    
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)  # Añade request.FILES
        if form.is_valid():
            form.save()
            return redirect('pet_catalog')
    else:
        form = PetForm()

    return render(request, 'create_pet.html', {'form': form})

def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet)  # Añade request.FILES
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pet_id=pet.id)
    else:
        form = PetForm(instance=pet)

    return render(request, 'update_pet.html', {'form': form, 'pet': pet})


def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'detail_pet.html', {'pet': pet})


def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.delete()
    return redirect('pet_catalog')  # Redirige al catálogo después de eliminar
