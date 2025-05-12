from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import PetLeverSignUpForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("pet_catalog") 

    if request.method == "POST":
        form = PetLeverSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente tras el registro
            return redirect("login")
    else:
        form = PetLeverSignUpForm()

    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")  # Redirigir al inicio si ya está autenticado

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("inicio")  # Redirigir a 'inicio' después del login exitoso
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")
