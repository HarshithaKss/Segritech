"""
Django management command to remove unwanted cleaning machines and keep only Segriwax.
This command removes AirClean AC-4000 Multi-Stage Cleaner and EcoClean EC-2000 Compact Cleaner
from the cleaning machines category, keeping only the Segriwax - Waxing & Cleaning Machine.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

from django.core.management.base import BaseCommand
from first.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Remove unwanted cleaning machines and keep only Segriwax'

    def handle(self, *args, **options):
        try:
            # Get the cleaning machines category
            cleaning_category = ProductCategory.objects.filter(category_type='cleaning_machines').first()
            
            if not cleaning_category:
                self.stdout.write(self.style.ERROR('Cleaning machines category not found.'))
                return

            # List of products to remove
            products_to_remove = [
                'AirClean AC-4000 Multi-Stage Cleaner',
                'EcoClean EC-2000 Compact Cleaner'
            ]

            # Remove the unwanted products
            removed_count = 0
            for product_name in products_to_remove:
                products = Product.objects.filter(
                    category=cleaning_category,
                    name__icontains=product_name.split()[0]  # Match by first word (AirClean, EcoClean)
                )
                
                for product in products:
                    self.stdout.write(f'Removing product: {product.name}')
                    product.delete()
                    removed_count += 1

            # Verify remaining products
            remaining_products = Product.objects.filter(category=cleaning_category, is_active=True)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully removed {removed_count} cleaning machines.'
                )
            )
            
            self.stdout.write('Remaining cleaning machines:')
            for product in remaining_products:
                self.stdout.write(f'  - {product.name}')

            if remaining_products.count() == 1 and 'Segriwax' in remaining_products.first().name:
                self.stdout.write(
                    self.style.SUCCESS('✓ Only Segriwax machine remains in cleaning machines category.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Please verify the remaining products are correct.')
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error cleaning up cleaning machines: {str(e)}')
            ) 