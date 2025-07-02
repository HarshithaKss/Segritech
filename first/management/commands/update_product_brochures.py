from django.core.management.base import BaseCommand
from django.core.files import File
from first.models import Product
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Updates product brochures from static/brochures directory'

    def handle(self, *args, **kwargs):
        # Map of product names to their brochure files
        brochure_mapping = {
            # Size Graders
            'Segritech Apple Size Grading Machine': 'Segritech Apple Size Grader_b.pdf',
            # Orange grader brochure is being prepared
            
            # Quality Graders
            'Multifruit Optical Grader': 'multifruit-optical-grader-brochure.pdf',
            
            # Weight Graders
            'Segritech : Weight Grader for Fruits': 'weight grading machine_b.pdf',
            
            # Cleaning Machines
            'Segriwax - Waxing & Cleaning Machine': 'segriwax-waxing-machine-brochure.pdf',
            
            # Packing Robots
            'SegriPack by Segritech': 'Segripack (1).pdf',
        }

        # Get absolute path to brochures directory
        brochures_dir = os.path.join(settings.BASE_DIR, 'static', 'brochures')
        self.stdout.write(f"Looking for brochures in: {brochures_dir}")
        
        # List all products first
        self.stdout.write("\nAvailable products in database:")
        for product in Product.objects.all():
            self.stdout.write(f"- {product.name}")
        
        self.stdout.write("\nProcessing brochures:")
        for product_name, brochure_file in brochure_mapping.items():
            try:
                # Try to get the product
                product = Product.objects.get(name=product_name)
                brochure_path = os.path.join(brochures_dir, brochure_file)
                
                self.stdout.write(f"\nProcessing {product_name}:")
                self.stdout.write(f"Looking for file: {brochure_path}")
                
                if os.path.exists(brochure_path):
                    self.stdout.write(f"Found brochure file: {brochure_file}")
                    
                    # Clear existing brochure if any
                    if product.brochure:
                        product.brochure.delete(save=False)
                    
                    # Add new brochure
                    with open(brochure_path, 'rb') as f:
                        product.brochure.save(brochure_file, File(f), save=True)
                    
                    # Verify the brochure was saved
                    product.refresh_from_db()
                    if product.brochure:
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Successfully added brochure for {product_name}')
                        )
                        self.stdout.write(f'  Brochure path: {product.brochure.path}')
                    else:
                        self.stdout.write(
                            self.style.ERROR(f'✗ Failed to save brochure for {product_name}')
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'✗ Brochure file not found: {brochure_path}')
                    )
            except Product.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'✗ Product not found: {product_name}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error updating brochure for {product_name}: {str(e)}')
                ) 