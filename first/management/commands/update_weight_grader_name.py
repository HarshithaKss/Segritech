"""
Django management command to rename the weight grader to "Segritech Weight Grading Machine".
This command updates the existing weight grader product name to the new Segritech branding.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Updates the name of the weight grader product'

    def handle(self, *args, **kwargs):
        try:
            # Get the weight graders category
            category = ProductCategory.objects.get(category_type='weight_graders')
            
            # List current products in weight graders category
            self.stdout.write("Weight graders category products before update:")
            for product in category.products.all():
                self.stdout.write(f"  - {product.name}")

            # Update PrecisionWeight WG-2500 to new name
            old_name = "PrecisionWeight WG-2500 Density Grader"
            new_name = "Segritech : Weight Grader for Fruits"
            
            try:
                product = Product.objects.get(name=old_name, category=category)
                
                # Update the name and slug
                product.name = new_name
                product.slug = slugify(new_name)
                product.save()
                
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully updated "{old_name}" to "{new_name}"'
                ))
                
                # Show updated products
                self.stdout.write("\nWeight graders category now has these products:")
                for product in category.products.all():
                    self.stdout.write(f"  - {product.name}")
                    
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'Product not found: {old_name}'
                ))
                
        except ProductCategory.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                'Weight graders category not found'
            )) 