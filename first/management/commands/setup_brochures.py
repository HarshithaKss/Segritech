"""
Management command to set up brochure files and handle missing files gracefully.
This ensures products without brochures don't cause errors.
"""

from django.core.management.base import BaseCommand
from django.core.files import File
from first.models import Product
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Set up brochure files and handle missing files gracefully'

    def find_brochure(self, filename):
        """Look for brochure file in multiple possible locations"""
        possible_paths = [
            os.path.join(settings.STATIC_ROOT, 'brochures', filename),  # /static/brochures/
            os.path.join(settings.BASE_DIR, 'static', 'brochures', filename),  # project/static/brochures/
            os.path.join(settings.BASE_DIR, 'brochures', filename),  # project/brochures/
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None

    def handle(self, *args, **options):
        self.stdout.write('Setting up brochure files...')
        
        # Map of product names to their brochure files
        brochure_mapping = {
            'Segritech Apple Size Grading Machine': 'Segritech Apple Size Grader_b.pdf',
            'Segritech Orange Grading Machine': None,  # No brochure yet
            'Multifruit Optical Grader': 'multifruit-optical-grader-brochure.pdf',
            'PrecisionWeight WG-2500 Density Grader': 'weight grading machine_b.pdf',
            'Segriwax - Waxing & Cleaning Machine': 'segriwax-waxing-machine-brochure.pdf',
            'SegriPack by Segritech': 'Segripack (1).pdf'
        }

        for product_name, brochure_filename in brochure_mapping.items():
            try:
                product = Product.objects.get(name=product_name)
                
                if not brochure_filename:
                    self.stdout.write(f'! No brochure available yet for {product_name}')
                    continue
                
                brochure_path = self.find_brochure(brochure_filename)
                if brochure_path:
                    with open(brochure_path, 'rb') as f:
                        product.brochure.save(brochure_filename, File(f), save=True)
                    self.stdout.write(
                        self.style.SUCCESS(f'✓ Set brochure for {product_name}: {brochure_filename}')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'! Brochure file not found for {product_name}: {brochure_filename}')
                    )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'! Product not found: {product_name}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'! Error setting brochure for {product_name}: {str(e)}')
                )

        self.stdout.write('\nBrochure setup completed!') 