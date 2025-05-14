from django.test import TestCase, Client
from django.urls import reverse
from .models import Pet

# Create your tests here.

# Test Class for Models
class PetModelTest(TestCase):

    def setUp(self):
        """
        Set up a Pet object for use in tests.
        This method runs before each test method (methods starting with 'test_').
        """
        # Create a sample Pet object
        # Use codes from your choices for species and gender
        Pet.objects.create(
            name="Buddy",
            species='PERRO',
            age=3,
            size="50",
            gender='MASCULINO',
            space_required="Patio",
            description="Perro juguetón y cariñoso",
            avilability=True
        )

    def test_pet_creation(self):
        """
        Test that a Pet object is created correctly.
        """
        # Retrieve the pet created in setUp
        buddy = Pet.objects.get(name="Buddy")

        # Assert that the attributes were set correctly
        self.assertEqual(buddy.species, 'PERRO')
        self.assertEqual(buddy.age, 3)
        self.assertEqual(buddy.gender, 'MASCULINO')
        self.assertTrue(buddy.avilability)

    def test_pet_str_method(self):
        """
        Test the _str_ method of the Pet model.
        """
        buddy = Pet.objects.get(name="Buddy")
        self.assertEqual(str(buddy), "Buddy")