import factory
from .models import Pet

class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    name = factory.Faker('name')
    species = factory.Faker('random_element', elements=['Perro', 'Gato', 'Ave', 'Conejo'])
    age = factory.Faker('random_int', min=0, max=20)
    size = factory.Faker('random_int', min=10, max=50)
    gender = factory.Faker('random_element', elements=['Macho', 'Hembra'])
    space_required = factory.Faker('random_element', elements=['Interior', 'Exterior' , 'Ambos', 'Jaridn'])
    description = factory.Faker('text')
    compatibility = factory.Faker('text')
    
