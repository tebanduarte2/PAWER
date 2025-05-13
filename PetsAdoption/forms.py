from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        required=False, 
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'size', 'gender', 'space_required', 'description','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'space_required': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
