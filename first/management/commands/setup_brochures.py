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
        
        # Map of product slugs to their brochure files
        brochure_mapping = {
            'inspection-box': 'Inspection box bro.pdf',
            'apple-size-grader': 'Segritech Apple Size Grader_b.pdf',
            'multifruit-optical-grader': 'quality_grader_b.pdf',
            'segritech-weight-grading-machine': 'weight grading machine_b.pdf',
            'cleaning-machine-1': 'cleaning-machine-brochure.pdf',
            'segriwax-waxing-cleaning-machine': 'Segriwax Waxing Machine.pdf',
            'segripack-by-segritech': 'Segripack (1).pdf',
        }
        
        # Get all products
        products = Product.objects.all()
        
        for product in products:
            try:
                # If product has a brochure mapping
                if product.slug in brochure_mapping:
                    brochure_filename = brochure_mapping[product.slug]
                    brochure_path = self.find_brochure(brochure_filename)
                    
                    # Check if brochure file exists in any location
                    if brochure_path:
                        with open(brochure_path, 'rb') as f:
                            product.brochure.save(brochure_filename, File(f), save=True)
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Set brochure for {product.name}: {brochure_filename} (found at {brochure_path})')
                        )
                    else:
                        # Clear brochure field if file doesn't exist
                        product.brochure = None
                        product.save()
                        self.stdout.write(
                            self.style.WARNING(f'! Brochure file not found for {product.name}: {brochure_filename}')
                        )
                else:
                    # Clear brochure field for products without mappings
                    product.brochure = None
                    product.save()
                    self.stdout.write(
                        self.style.WARNING(f'! No brochure mapping for {product.name}')
                    )
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error setting brochure for {product.name}: {str(e)}')
                )
                
        self.stdout.write(self.style.SUCCESS('\nBrochure setup completed!')) 