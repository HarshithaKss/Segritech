"""
Django management command to shorten all product descriptions to 4-5 lines.
This command runs all description shortening commands in sequence.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Shorten all product descriptions to 4-5 lines'

    def handle(self, *args, **options):
        try:
            # Shorten Segriwax description
            self.stdout.write('Shortening Segriwax description...')
            call_command('shorten_segriwax_description')
            
            # Shorten SegriPack description
            self.stdout.write('Shortening SegriPack description...')
            call_command('shorten_segripack_description')
            
            self.stdout.write(self.style.SUCCESS('Successfully shortened all product descriptions'))
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error shortening descriptions: {str(e)}')
            ) 