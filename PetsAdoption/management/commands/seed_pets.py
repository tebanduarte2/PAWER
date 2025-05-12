from django.core.management.base import BaseCommand
from PetsAdoption.factories import PetFactory

class Command(BaseCommand):
    help = 'Seed the database with initial pet data'

    def handle(self, *args, **options):  # You can change this number to seed more or fewer pets
        PetFactory.create_batch(20)
        self.stdout.write(self.style.SUCCESS('Successfully seeded comments'))