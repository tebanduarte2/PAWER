from django.shortcuts import render
from .forms import CompatibilityTestForm
from PetsAdoption.models import Pet


def compatibility_test(request):
    if request.method == 'POST':
        form = CompatibilityTestForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data
            compatible_pets = filter_pets(answers)
            return render(request, 'compatibility_results.html', {'pets': compatible_pets})
        else:
            return render(request, 'compatibility_form.html', {'form': form})
    else:
        form = CompatibilityTestForm()
    return render(request, 'compatibility_form.html', {'form': form})


def filter_pets(answers):
    puntos_perro = 0
    puntos_gato = 0
    puntos_pajaro = 0
    puntos_hamster = 0
    puntos_conejo = 0

    personalidad = answers.get('pregunta_personalidad')
    if personalidad == 'tranquilo':
        puntos_gato += 2
        puntos_conejo += 2
        puntos_hamster += 1
        puntos_pajaro += 1
    elif personalidad == 'jugueton':
        puntos_perro += 2
        puntos_gato += 1
        puntos_conejo += 1
    elif personalidad == 'cariñoso':
        puntos_perro += 3
        puntos_gato += 2
        puntos_pajaro += 1
    elif personalidad == 'independiente':
        puntos_gato += 2
        puntos_hamster += 2
        puntos_pajaro += 2
        puntos_conejo += 1

    espacio = answers.get('pregunta_espacio')
    if espacio == 'pequeno':
        puntos_gato += 2
        puntos_hamster += 2
        puntos_pajaro += 2
        puntos_conejo += 1
    elif espacio == 'mediano':
        puntos_perro += 1
        puntos_gato += 1
        puntos_conejo += 2
        puntos_pajaro += 2
    elif espacio == 'grande':
        puntos_perro += 2
        puntos_conejo += 1

    tiempo = answers.get('pregunta_tiempo')
    if tiempo == 'poco':
        puntos_gato += 1
        puntos_hamster += 2
        puntos_pajaro += 2
    elif tiempo == 'medio':
        puntos_perro += 1
        puntos_gato += 1
        puntos_conejo += 1
        puntos_hamster += 2
        puntos_pajaro += 2
    elif tiempo == 'mucho':
        puntos_perro += 2
        puntos_gato += 2
        puntos_conejo += 2
        puntos_hamster += 2
        puntos_pajaro += 2

    otros_animales = answers.get('pregunta_otros_animales')
    if otros_animales == 'si':
        puntos_perro += 1
        puntos_gato += 1
    elif otros_animales == 'no':
        puntos_pajaro += 1
        puntos_hamster += 1
        puntos_conejo += 1

    genero = answers.get('pregunta_genero')

    tamaño_maximo = answers.get('pregunta_tamaño_maxima')
    pets = Pet.objects.all()
    if tamaño_maximo == '30':
        filtro_tamaño = pets.filter(size__lte='30')
    elif tamaño_maximo == '50':
        filtro_tamaño = pets.filter(size__lte='50') 
    elif tamaño_maximo == '0':
        filtro_tamaño = pets.filter(ize__gte='0')

    ruido = answers.get('pregunta_ruido')
    if ruido == 'tolerante':
        puntos_perro += 2
        puntos_gato += 2
        puntos_pajaro += 2
        puntos_hamster += 2
        puntos_conejo += 2
    elif ruido == 'moderado':
        puntos_gato += 2
        puntos_conejo += 2
        puntos_hamster += 2
    elif ruido == 'sensible':
        puntos_hamster += 2
        puntos_conejo += 2
        puntos_gato += 2

    niños = answers.get('pregunta_niños')
    if niños == 'si':
        puntos_perro += 2
        puntos_conejo += 1
        puntos_gato += 1
    elif niños == 'no':
        puntos_pajaro += 1
        puntos_hamster += 1

    cuidados = answers.get('pregunta_cuidados')
    if cuidados == 'poco':
        puntos_gato += 1
        puntos_hamster += 1
        puntos_pajaro += 1
    elif cuidados == 'moderado':
        puntos_perro += 1
        puntos_gato += 2
        puntos_conejo += 2
        puntos_pajaro += 2
    elif cuidados == 'mucho':
        puntos_perro += 2
        puntos_gato += 2
        puntos_conejo += 2
        puntos_pajaro += 2

    dieta = answers.get('pregunta_dieta')
    if niños == 'si':
        puntos_perro += 2
        puntos_gato += 2
        puntos_pajaro += 1
        puntos_hamster += 1
    elif niños == 'no':
        puntos_pajaro += 1
        puntos_hamster += 1
        puntos_conejo += 2
        
    alergia = answers.get('pregunta_alergia')
    especificar_alergia = answers.get('especificar_alergia')
    filtro_alergia = False
    if alergia == 'si' and especificar_alergia:
        filtro_alergia = pets.exclude(species__icontains=especificar_alergia.lower())

    puntuaciones = {
        'perro': puntos_perro,
        'gato': puntos_gato,
        'pajaro': puntos_pajaro,
        'hamster': puntos_hamster,
        'conejo': puntos_conejo,
    }
    mascota_compatible = max(puntuaciones, key=puntuaciones.get)

    if filtro_alergia:
        compatible_pets = Pet.objects.filter(species__iexact=mascota_compatible) & filtro_tamaño & filtro_alergia
    else:
        compatible_pets = Pet.objects.filter(species__iexact=mascota_compatible) & filtro_tamaño

    return compatible_pets