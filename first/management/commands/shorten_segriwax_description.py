from django.core.management.base import BaseCommand
from first.models import Product

class Command(BaseCommand):
    help = 'Shorten the Segriwax machine description'

    def handle(self, *args, **options):
        try:
            # Find product by name
            product_name = "Segriwax - Waxing & Cleaning Machine"
            
            product = Product.objects.get(name=product_name)
            
            # Update description with shorter version
            new_description = '''Segriwax™ - Next-Generation Fruit Cleaning and Waxing Machine by Segritech

A compact, portable solution that brings industrial-grade cleaning and waxing capabilities to India's post-harvest ecosystem. Perfect for farmers, cooperatives, and exporters looking to enhance produce shelf life and achieve retail-grade presentation.

Designed for efficiency and mobility, Segriwax combines advanced cleaning technology with precision waxing application to ensure your fresh produce meets international quality standards.

Features easy operation with minimal training required and delivers professional-grade results in an affordable package.'''
            
            product.detailed_description = new_description
            
            # Save changes
            product.save()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully shortened Segriwax description'))
            
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Product "{product_name}" not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating product: {str(e)}')) 