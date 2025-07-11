"""
Django management command to rename the Multifruit Optical Grader to "Segritech Minisort".
This command updates the existing quality grader product name to the new branding.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import Product, ProductCategory

class Command(BaseCommand):
    help = 'Rename Multifruit Optical Grader to Segritech Minisort'

    def handle(self, *args, **options):
        try:
            # Get the quality graders category
            quality_category = ProductCategory.objects.filter(category_type='quality_graders').first()
            
            if not quality_category:
                self.stdout.write(self.style.ERROR('Quality graders category not found.'))
                return

            # Find the existing quality grader product by old slug
            quality_grader = Product.objects.filter(
                category=quality_category,
                slug='multifruit-optical-grader'
            ).first()

            if not quality_grader:
                # Try finding by current name if old slug not found
                quality_grader = Product.objects.filter(
                    category=quality_category,
                    name='Segritech Minisort'
                ).first()

            if quality_grader:
                # Update product details
                old_name = quality_grader.name
                old_slug = quality_grader.slug
                quality_grader.name = 'Segritech Minisort'
                quality_grader.slug = 'segritech-minisort'
                
                # Save the updated product
                quality_grader.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully updated product:\n'
                        f'Name: "{old_name}" -> "Segritech Minisort"\n'
                        f'Slug: "{old_slug}" -> "segritech-minisort"'
                    )
                )
            else:
                self.stdout.write(self.style.WARNING('No quality grader product found to update'))

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating quality grader: {str(e)}')
            ) 