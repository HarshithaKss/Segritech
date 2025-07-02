"""
Django management command to add Segriwax Waxing & Cleaning Machine to the cleaning machines category.
This command adds the compact, portable, high-speed cleaning & waxing system for fresh produce
with detailed specifications, features, and brochure integration.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import ProductCategory, Product


class Command(BaseCommand):
    help = 'Add Segriwax Waxing & Cleaning Machine to the cleaning machines category'

    def handle(self, *args, **options):
        try:
            # Get the cleaning machines category
            cleaning_category = ProductCategory.objects.filter(category_type='cleaning_machines').first()
            
            if not cleaning_category:
                self.stdout.write(self.style.ERROR('Cleaning machines category not found. Please run setup_categories first.'))
                return

            # Check if Segriwax already exists
            slug = slugify('Segriwax Waxing Cleaning Machine')
            if Product.objects.filter(slug=slug).exists():
                self.stdout.write(self.style.WARNING('Segriwax machine already exists. Updating...'))
                segriwax = Product.objects.get(slug=slug)
            else:
                segriwax = Product()

            # Product details
            segriwax.category = cleaning_category
            segriwax.name = 'Segriwax - Waxing & Cleaning Machine'
            segriwax.slug = slug
            segriwax.short_description = 'Compact, Portable, High-Speed Cleaning & Waxing System for Fresh Produce'
            
            segriwax.detailed_description = '''Segriwax™ - Next-Generation Fruit Cleaning and Waxing Machine by Segritech

Segriwax™ is a next-generation fruit cleaning and waxing machine tailored for India's decentralized post-harvest ecosystem. Designed for efficiency, affordability, and mobility, Segriwax brings industrial grade performance into a compact, field-deployable solution.

Whether you're a farmer looking to enhance shelf life, or an exporter aiming for retail-grade presentation — Segriwax delivers the finish your produce deserves.

PRODUCT INTRODUCTION:
Segriwax™ is specifically designed for India's diverse agricultural landscape, offering professional-grade cleaning and waxing capabilities in a portable, cost-effective package. This machine combines advanced cleaning technology with precision waxing application to ensure your fresh produce meets international quality standards.

KEY BENEFITS:
• Enhanced shelf life of fresh produce
• Retail-grade presentation for premium markets
• Compact and portable design for field deployment
• Industrial-grade performance in affordable package
• Suitable for farmers, cooperatives, and exporters
• Easy operation with minimal training required'''

            # Key features
            segriwax.key_features = json.dumps([
                'Next-generation cleaning and waxing technology',
                'Compact and portable design',
                'High-speed processing capability',
                'Industrial-grade performance',
                'Field-deployable solution',
                'Cost-effective operation',
                'Enhanced shelf life for produce',
                'Retail-grade finish quality',
                'Easy maintenance and operation',
                'Suitable for various fruit types'
            ])

            # Specifications
            segriwax.specifications = json.dumps({
                'Type': 'Cleaning & Waxing Machine',
                'Model': 'Segriwax™',
                'Design': 'Compact & Portable',
                'Performance': 'Industrial Grade',
                'Application': 'Fresh Produce Processing',
                'Deployment': 'Field Ready',
                'Operation': 'High-Speed Processing',
                'Target Market': 'Farmers, Cooperatives, Exporters',
                'Finish Quality': 'Retail Grade',
                'Maintenance': 'Easy & Minimal'
            })

            # Applications
            segriwax.applications = json.dumps([
                'Small to medium farm operations',
                'Agricultural cooperatives',
                'Export packaging centers',
                'Fresh produce processing units',
                'Fruit packhouses',
                'Post-harvest processing facilities',
                'Regional collection centers',
                'Farmer producer organizations'
            ])

            # Benefits
            segriwax.benefits = json.dumps([
                'Enhanced shelf life of fresh produce',
                'Premium market presentation',
                'Reduced post-harvest losses',
                'Improved market pricing',
                'Professional finish quality',
                'Portable field deployment',
                'Cost-effective processing',
                'Easy operation and maintenance',
                'Suitable for decentralized operations',
                'Meets international quality standards'
            ])

            # Other details
            segriwax.price_range = 'Contact for Pricing'
            segriwax.lead_time = ''
            segriwax.is_featured = True
            segriwax.is_active = True
            
            # SEO details
            segriwax.meta_title = 'Segriwax Waxing & Cleaning Machine | Segritech Fresh Produce Processing'
            segriwax.meta_description = 'Segriwax™ by Segritech - Compact, portable, high-speed cleaning & waxing system for fresh produce. Industrial-grade performance for enhanced shelf life and retail presentation.'

            # Save the product
            segriwax.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully added Segriwax Waxing & Cleaning Machine to cleaning machines category'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error adding Segriwax machine: {str(e)}')
            ) 