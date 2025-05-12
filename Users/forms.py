from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PetLever

class PetLeverSignUpForm(UserCreationForm):
    name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Dirección", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    cellphone = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = PetLever
        fields = ["username", "name", "address", "cellphone", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control'}),
        }
