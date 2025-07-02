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
    help = 'Rename weight grader to Segritech Weight Grading Machine'

    def handle(self, *args, **options):
        try:
            # Get the weight graders category
            weight_category = ProductCategory.objects.filter(category_type='weight_graders').first()
            
            if not weight_category:
                self.stdout.write(self.style.ERROR('Weight graders category not found.'))
                return

            # Find the existing weight grader product
            weight_grader = Product.objects.filter(category=weight_category).first()

            if weight_grader:
                # Update product details
                old_name = weight_grader.name
                weight_grader.name = 'Segritech Weight Grading Machine'
                weight_grader.slug = slugify('Segritech Weight Grading Machine')
                weight_grader.short_description = 'High-precision weight-based grading machine for export-quality sorting and classification'
                
                weight_grader.detailed_description = '''Segritech Weight Grading Machine - Precision Weight-Based Sorting System

The Segritech Weight Grading Machine delivers exceptional accuracy in weight-based grading, essential for export markets requiring strict weight specifications. This advanced system uses precision load cells and intelligent sorting algorithms to classify produce into precise weight categories.

Built for Indian agricultural operations, it ensures consistent weight standards for premium packaging and export compliance. Whether you're grading fruits, vegetables, or specialty crops, this machine provides reliable, accurate sorting for enhanced market value.

Features precision weighing technology, multiple weight category outputs, and robust construction designed for continuous operation in demanding agricultural environments.'''

                # Update key features
                weight_grader.key_features = json.dumps([
                    'Precision weighing ±0.1g accuracy',
                    'Multiple weight category outputs',
                    'Export quality standards compliance',
                    'Advanced load cell technology',
                    'Vibration dampening system',
                    'Digital weight display and controls',
                    'Robust construction for continuous use',
                    'Easy operation and maintenance',
                    'Food-grade materials',
                    'Customizable weight ranges'
                ])

                # Update specifications
                weight_grader.specifications = json.dumps({
                    'Model': 'Segritech WGM-2000',
                    'Processing Capacity': '500-800 kg/hour',
                    'Weighing Accuracy': '±0.1g',
                    'Weight Range': '5g - 500g per unit',
                    'Power Consumption': '5 kW',
                    'Dimensions': '2.5m x 1.8m x 2.0m',
                    'Weight': '850 kg',
                    'Construction': 'Food-grade stainless steel',
                    'Control System': 'Digital touchscreen interface'
                })

                # Update applications
                weight_grader.applications = json.dumps([
                    'Export preparation facilities',
                    'Premium fruit processing',
                    'Vegetable grading operations',
                    'Quality certification centers',
                    'Agricultural cooperatives',
                    'Commercial packaging lines',
                    'Specialty crop sorting',
                    'High-value produce grading'
                ])

                # Update benefits
                weight_grader.benefits = json.dumps([
                    'Enhanced export market access',
                    'Consistent weight specifications',
                    'Premium pricing for graded produce',
                    'Reduced manual sorting labor',
                    'Improved product presentation',
                    'Quality compliance assurance',
                    'Increased operational efficiency',
                    'Better customer satisfaction'
                ])

                # Update other details
                weight_grader.price_range = 'Contact for Pricing'
                weight_grader.lead_time = ''
                weight_grader.is_featured = True
                weight_grader.is_active = True
                
                # Update SEO details
                weight_grader.meta_title = 'Segritech Weight Grading Machine | Precision Weight-Based Sorting'
                weight_grader.meta_description = 'Segritech Weight Grading Machine - High-precision weight-based sorting for export-quality classification. Advanced load cell technology with ±0.1g accuracy.'

                # Save the updated product
                weight_grader.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully updated "{old_name}" to "Segritech Weight Grading Machine"'
                    )
                )
            else:
                self.stdout.write(self.style.WARNING('No weight grader product found to update'))

            # Show final count
            remaining_products = Product.objects.filter(category=weight_category, is_active=True)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Weight graders category now has {remaining_products.count()} products:'
                )
            )

            # List products
            for product in remaining_products:
                self.stdout.write(f'  - {product.name}')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating weight grader: {str(e)}')
            ) 