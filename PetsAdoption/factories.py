import factory
from .models import Pet

class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    name = factory.Faker('random_element', elements=["Luna", "Sol", "Milo", "Lola", "Simón", "Nina", "Romeo", "Cleo", "Oliver", "Mía",
    "Coco", "Kiara", "Leo", "Nala", "Tigre", "Zoe", "Salem", "Frida", "Bowie", "Alma",
    "Max", "Bella", "Rocky", "Lucy", "Toby", "Daisy", "Duke", "Luna", "Cooper", "Sadie",
    "Buddy", "Penny", "Charlie", "Ruby", "Teddy", "Sophie", "Jack", "Mia", "Oliver", "Chloe",
    "Pío", "Azul", "Canela", "Coco", "Jade", "Kiwi", "Mango", "Nube", "Ónix", "Paz",
    "Rayo", "Sol", "Turquesa", "Violeta", "Zafiro", "Alba", "Brisas", "Cielo", "Coral", "Eco",
    "Blanco", "Oreo", "Trufa", "Nieve", "Chocolate", "Canela", "Miel", "Pelusa", "Tambor", "Ceniza",
    "Caramelo", "Diente", "Jumpy", "Muffin", "Pipo", "Rosita", "Veloz", "Zanahoria", "Brisa", "Copito"])
    species = factory.Faker('random_element', elements=['Perro', 'Gato', 'Ave', 'Conejo'])
    age = factory.Faker('random_int', min=1, max=15)
    size = factory.Faker('random_int', min=10, max=50)
    gender = factory.Faker('random_element', elements=['Macho', 'Hembra'])
    space_required = factory.Faker('random_element', elements=['Interior', 'Exterior' , 'Ambos', 'Jardin'])
    description = factory.Faker('random_element', elements=["Un compañero leal y cariñoso, siempre dispuesto a jugar.",
    "Adora las siestas y los mimos, un verdadero ronroneador profesional.",
    "Pequeño y lleno de energía, le encanta explorar y gorjear melodías.",
    "Suave y tranquilo, disfruta de las caricias y los momentos de paz.",
    "Juguetón y curioso, siempre atento a lo que sucede a su alrededor.",
    "Una adorable criatura en busca de un hogar lleno de amor y cuidados.",
    "Inteligente y vivaz, aprende rápido y le encanta interactuar.",
    "Independiente pero afectuoso, te brindará su cariño a su manera.",
    "Con un espíritu aventurero, ideal para familias activas.",
    "Dulce y gentil, perfecto para un hogar tranquilo.",
    "Siempre alegre y moviendo la cola, te recibirá con entusiasmo.",
    "Un pequeño tesoro peludo que llenará tu vida de alegría.",
    "Le encanta acurrucarse y pasar tiempo cerca de sus humanos.",
    "Con una personalidad única que te encantará descubrir.",
    "Busca un hogar donde pueda sentirse seguro y amado.",
    "Un amigo fiel que te acompañará en todas tus aventuras.",
    "Disfruta de los juegos y las探索, un espíritu joven.",
    "Alegre y sociable, se lleva bien con otros animales y personas.",
    "Con unos ojos tiernos que te robarán el corazón.",
    "Un miembro más de la familia esperando ser adoptado.",
    "Le gusta observar el mundo desde su ventana, tranquilo y curioso.",
    "Brinda consuelo y compañía, un apoyo emocional incondicional.",
    "Necesita un hogar paciente y amoroso para florecer.",
    "Te sorprenderá con sus travesuras y su cariño incondicional.",
    "Un pequeño saltarín lleno de vitalidad.",
    "Busca un compañero humano para compartir juegos y afecto.",
    "Su ronroneo es la melodía más dulce.",
    "Con plumas suaves y un canto melodioso.",
    "Un pelaje suave y unos bigotes curiosos.",
    "Sus orejas largas son irresistibles.",
    "Siempre listo para una sesión de juegos interactivos.",
    "Te seguirá por toda la casa, buscando tu compañía.",
    "Le encanta recibir atención y caricias suaves.",
    "Con un carácter dulce y adaptable."])
    
