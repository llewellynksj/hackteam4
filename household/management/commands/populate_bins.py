from django.core.management.base import BaseCommand
from household.models import Bin

class Command(BaseCommand):
    help = 'Populates the Bin model with hardcoded choices'

    def handle(self, *args, **options):
        Bin.populate_bins()
        self.stdout.write(self.style.SUCCESS('Bins populated successfully!'))