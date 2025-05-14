from django import forms

class CompatibilityTestForm(forms.Form):
    PERSONALITY_CHOICES = [
        ('tranquilo', 'Tranquilo y relajado'),
        ('jugueton', 'Juguetón y activo'),
        ('cariñoso', 'Cariñoso y dependiente'),
        ('independiente', 'Independiente y curioso'),
    ]
    SPACE_CHOICES = [
        ('pequeno', 'Espacio pequeño (apartamento)'),
        ('mediano', 'Espacio mediano (casa con patio pequeño)'),
        ('grande', 'Espacio grande (casa con jardín amplio)'),
    ]
    TIME_CHOICES = [
        ('poco', 'Poco tiempo para dedicar'),
        ('medio', 'Tiempo moderado para dedicar'),
        ('mucho', 'Mucho tiempo para dedicar'),
    ]
    YES_NO_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]
    GENDER_CHOICES = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
    ]
    SIZE_CHOICES = [
        ('30', 'Máximo 30 cm'),
        ('50', 'Máximo 50 cm'),
        ('0', 'Sin límite de tamaño'),
    ]
    NOISE_CHOICES = [
        ('tolerante', 'Soy bastante tolerante al ruido y al desorden'),
        ('moderado', 'Prefiero un ambiente relativamente tranquilo y ordenado'),
        ('sensible', 'Soy sensible al ruido y prefiero un ambiente muy ordenado'),
    ]
    CARE_CHOICES = [
        ('poco', 'Poco tiempo y esfuerzo'),
        ('moderado', 'Tiempo y esfuerzo moderado'),
        ('mucho', 'Mucho tiempo y esfuerzo'),
    ]
    PREGUNTA_ALERGIA_CHOICES = [
        ('perro', 'Perros'),
        ('gato', 'Gatos'),
        ('pajaro', 'Pajaros'),
        ('hamster', 'Hamster'),
        ('conejo', 'Conejo'),
    ]
    
    pregunta_personalidad = forms.ChoiceField(
        label='¿Qué tipo de mascota buscas?',
        choices=PERSONALITY_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_espacio = forms.ChoiceField(
        label='¿Qué tipo de espacio tienes disponible?',
        choices=SPACE_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_tiempo = forms.ChoiceField(
        label='¿Cuánto tiempo puedes dedicar a tu mascota diariamente?',
        choices=TIME_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_otros_animales = forms.ChoiceField(
        label='¿Tienes otras mascotas?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_genero = forms.ChoiceField(
        label='¿De cuál género preferirías tu mascota?',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_tamaño_maxima = forms.ChoiceField(
        label='¿Cuál es el tamaño máximo para tu mascota?',
        choices=SIZE_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_ruido = forms.ChoiceField(
        label='¿Cómo reaccionas ante el ruido y el desorden?',
        choices=NOISE_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_niños = forms.ChoiceField(
        label='¿Tienes niños pequeños en casa?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_cuidados = forms.ChoiceField(
        label='¿Cuánto tiempo y esfuerzo puedes dedicar al aseo de tu mascota?',
        choices=CARE_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_dieta = forms.ChoiceField(
        label='¿Te importa tener una mascota que requiera una dieta específica?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
    pregunta_alergia = forms.ChoiceField(
        label='¿Tienes alguna alergia a algún tipo de animal?',
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect
    )
    especificar_alergia = forms.ChoiceField(
        label='Especifica la alergia',
        choices=PREGUNTA_ALERGIA_CHOICES,
        required=False,
        widget=forms.Select,
    )
    
    def clean(self):
        cleaned_data = super().clean()
        tiene_alergia = cleaned_data.get('tiene_alergia')
        especificar_alergia = cleaned_data.get('especificar_alergia')

        if tiene_alergia == 'si' and not especificar_alergia:
            self.add_error('especificar_alergia', 'Por favor, especifica a qué tipo de animal tienes alergia.')

        return cleaned_data
