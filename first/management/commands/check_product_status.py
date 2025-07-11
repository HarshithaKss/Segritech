"""
Django management command to check the current state of products in the database.
This will help diagnose URL routing issues.
"""

from django.core.management.base import BaseCommand
from first.models import Product, ProductCategory

class Command(BaseCommand):
    help = 'Check current state of products in the database'

    def handle(self, *args, **options):
        try:
            # Get the quality graders category
            quality_category = ProductCategory.objects.filter(category_type='quality_graders').first()
            
            if not quality_category:
                self.stdout.write(self.style.ERROR('Quality graders category not found.'))
                return

            self.stdout.write("\nQuality Graders Category:")
            self.stdout.write(f"Name: {quality_category.name}")
            self.stdout.write(f"Slug: {quality_category.slug}")
            
            # List all products in the category
            self.stdout.write("\nProducts in Quality Graders category:")
            products = Product.objects.filter(category=quality_category)
            
            if not products:
                self.stdout.write(self.style.WARNING('No products found in this category'))
            
            for product in products:
                self.stdout.write(f"\nProduct Details:")
                self.stdout.write(f"  Name: {product.name}")
                self.stdout.write(f"  Slug: {product.slug}")
                self.stdout.write(f"  Category: {product.category.name}")
                self.stdout.write(f"  Active: {product.is_active}")
                self.stdout.write(f"  Featured: {product.is_featured}")

            # Also check if any product has the old slug
            old_product = Product.objects.filter(slug='multifruit-optical-grader').first()
            if old_product:
                self.stdout.write("\nFound product with old slug:")
                self.stdout.write(f"  Name: {old_product.name}")
                self.stdout.write(f"  Slug: {old_product.slug}")
                self.stdout.write(f"  Category: {old_product.category.name}")

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error checking products: {str(e)}')
            ) 