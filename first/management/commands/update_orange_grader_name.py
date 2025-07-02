"""
Django management command to rename the Orange Grader to "Segritech Orange Grading Machine".
This command updates the existing orange grader product name to the new Segritech branding.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Rename Orange Grader to Segritech Orange Grading Machine'

    def handle(self, *args, **options):
        try:
            # Get the size graders category
            size_category = ProductCategory.objects.filter(category_type='size_graders').first()
            
            if not size_category:
                self.stdout.write(self.style.ERROR('Size graders category not found.'))
                return

            # Find the existing orange grader product
            orange_grader = Product.objects.filter(
                category=size_category, 
                name='Orange Grader'
            ).first()

            if orange_grader:
                # Update product details
                old_name = orange_grader.name
                orange_grader.name = 'Segritech Orange Grading Machine'
                orange_grader.slug = slugify('Segritech Orange Grading Machine')
                orange_grader.short_description = 'Compact size grading machine designed specifically for oranges with reliable performance and space efficiency'
                
                orange_grader.detailed_description = '''Segritech Orange Grading Machine - Specialized Citrus Sorting System

The Segritech Orange Grading Machine is specifically designed for orange grading operations, offering precision sizing in a space-efficient design. Built for Indian agricultural operations, this compact machine delivers reliable performance for cooperative societies, small processing units, and citrus specialty graders.

Features advanced mechanical sorting technology optimized for orange characteristics, ensuring consistent size classification while maintaining fruit quality. The system provides cost-effective sorting solutions with durable construction designed for continuous operation in agricultural environments.

Perfect for operations requiring dedicated orange processing with space constraints and budget considerations.'''

                # Update key features
                orange_grader.key_features = json.dumps([
                    'Compact design for space efficiency',
                    'Processing capacity: 250kg/hour',
                    'Easy maintenance and operation',
                    'Cost-effective solution',
                    'Durable construction',
                    'Low power consumption',
                    'Optimized for orange characteristics',
                    'Consistent size classification',
                    'Simple controls and operation',
                    'Portable design'
                ])

                # Update specifications
                orange_grader.specifications = json.dumps({
                    'Model': 'Segritech OGM-250',
                    'Processing Capacity': '250 kg/hour',
                    'Accuracy': '98.5%',
                    'Power Consumption': '3.0 kW',
                    'Dimensions': '1.8m x 1.2m x 1.5m',
                    'Weight': '450 kg',
                    'Material': 'Mild Steel with food-grade coating',
                    'Output Grades': '3-5 size categories',
                    'Voltage': '220V/440V, 50 Hz'
                })

                # Update applications
                orange_grader.applications = json.dumps([
                    'Small processing units',
                    'Cooperative societies',
                    'Specialty crop grading',
                    'Regional distribution centers',
                    'Citrus packaging facilities',
                    'Local market preparation',
                    'Export pre-processing',
                    'Farm-level grading'
                ])

                # Update benefits
                orange_grader.benefits = json.dumps([
                    'Lower initial investment',
                    'Space-efficient design',
                    'Reliable performance',
                    'Easy to operate',
                    'Reduced labor costs',
                    'Consistent grading quality',
                    'Improved market pricing',
                    'Quick return on investment'
                ])

                # Update other details
                orange_grader.price_range = '₹25,000 - ₹32,000'
                orange_grader.lead_time = ''
                orange_grader.is_featured = False
                orange_grader.is_active = True
                
                # Update SEO details
                orange_grader.meta_title = 'Segritech Orange Grading Machine | Compact Citrus Sorting'
                orange_grader.meta_description = 'Segritech Orange Grading Machine - Compact, cost-effective orange sorting solution. 250kg/hour capacity with 98.5% accuracy for small processing units.'

                # Save the updated product
                orange_grader.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully updated "{old_name}" to "Segritech Orange Grading Machine"'
                    )
                )
            else:
                self.stdout.write(self.style.WARNING('No orange grader product found to update'))

            # Show final count
            remaining_products = Product.objects.filter(category=size_category, is_active=True)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Size graders category now has {remaining_products.count()} products:'
                )
            )

            # List products
            for product in remaining_products:
                self.stdout.write(f'  - {product.name}')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating orange grader: {str(e)}')
            ) 