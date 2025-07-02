"""
Django management command to update packing robots - rename one to SegriPack and remove the other.
This command updates the RoboPack RP-5000 to "SegriPack by Segritech - Smart Robotic Packing System for Graded Fresh Produce"
and removes the FlexiPack FP-3000 Semi-Automated Packer.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import Product, ProductCategory


class Command(BaseCommand):
    help = 'Update packing robots - rename one to SegriPack and remove the other'

    def handle(self, *args, **options):
        try:
            # Get the packing robots category
            packing_category = ProductCategory.objects.filter(category_type='packing_robots').first()
            
            if not packing_category:
                self.stdout.write(self.style.ERROR('Packing robots category not found.'))
                return

            # Remove FlexiPack FP-3000
            flexipack_products = Product.objects.filter(
                category=packing_category,
                name__icontains='FlexiPack'
            )
            
            removed_count = 0
            for product in flexipack_products:
                self.stdout.write(f'Removing product: {product.name}')
                product.delete()
                removed_count += 1

            # Update RoboPack to SegriPack
            robopack_product = Product.objects.filter(
                category=packing_category,
                name__icontains='RoboPack'
            ).first()

            if robopack_product:
                # Update product details
                robopack_product.name = 'SegriPack by Segritech'
                robopack_product.slug = slugify('SegriPack by Segritech')
                robopack_product.short_description = 'Smart Robotic Packing System for Graded Fresh Produce'
                
                robopack_product.detailed_description = '''SegriPack by Segritech - Smart Robotic Packing System for Graded Fresh Produce

SegriPack is Segritech's flagship automated packaging solution designed specifically for graded fresh produce. This intelligent robotic system combines precision handling with smart weighing technology to deliver consistent, retail-ready packaging for fruits and vegetables.

Built for Indian agricultural operations, SegriPack offers the perfect balance of automation, reliability, and cost-effectiveness. Whether you're packaging pomegranates, apples, citrus fruits, or other fresh produce, SegriPack ensures professional presentation while reducing labor dependency.

KEY FEATURES:
• Smart robotic arms with gentle produce handling
• Integrated precision weighing system
• Multi-format packaging capability (bags, trays, boxes)
• Vision-guided quality control
• Real-time production monitoring
• Food-grade construction materials
• Easy operation with minimal training

BENEFITS:
• Consistent packaging quality and presentation
• Reduced labor costs and dependency
• Increased packaging speed and throughput
• Minimized product damage during handling
• Enhanced food safety and hygiene standards
• Improved operational efficiency'''

                # Update key features
                robopack_product.key_features = json.dumps([
                    'Smart robotic arm automation',
                    'Precision weighing and portioning',
                    'Multi-format packaging capability',
                    'Vision-guided quality control',
                    'Gentle produce handling technology',
                    'Food-grade construction materials',
                    'Real-time production monitoring',
                    'Easy operation interface',
                    'Minimal training requirement',
                    'Consistent packaging quality'
                ])

                # Update specifications
                robopack_product.specifications = json.dumps({
                    'Model': 'SegriPack SP-2000',
                    'Packaging Speed': '150-200 packages/hour',
                    'Weight Range': '0.5kg - 25kg',
                    'Weight Accuracy': '±2g',
                    'Package Formats': 'Bags, trays, boxes, nets',
                    'Produce Types': 'Fruits, vegetables, graded produce',
                    'Power Consumption': '8 kW',
                    'Dimensions': '3.5m x 2.5m x 2.2m',
                    'Construction': 'Food-grade stainless steel',
                    'Control System': 'PLC with touchscreen interface'
                })

                # Update applications
                robopack_product.applications = json.dumps([
                    'Fresh produce packaging facilities',
                    'Export packaging centers',
                    'Agricultural cooperatives',
                    'Commercial fruit processing',
                    'Vegetable packing houses',
                    'Retail packaging operations',
                    'Graded produce packaging',
                    'Quality-controlled packaging lines'
                ])

                # Update benefits
                robopack_product.benefits = json.dumps([
                    'Consistent retail-ready packaging',
                    'Reduced labor dependency',
                    'Enhanced food safety compliance',
                    'Increased packaging throughput',
                    'Minimized product damage',
                    'Improved operational efficiency',
                    'Professional package presentation',
                    'Cost-effective automation solution'
                ])

                # Update other details
                robopack_product.price_range = 'Contact for Pricing'
                robopack_product.lead_time = ''
                robopack_product.is_featured = True
                robopack_product.is_active = True
                
                # Update SEO details
                robopack_product.meta_title = 'SegriPack by Segritech | Smart Robotic Packing System for Fresh Produce'
                robopack_product.meta_description = 'SegriPack - Smart robotic packing system for graded fresh produce. Automated packaging with precision weighing, gentle handling, and consistent quality presentation.'

                # Save the updated product
                robopack_product.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully updated RoboPack to SegriPack by Segritech'
                    )
                )
            else:
                self.stdout.write(self.style.WARNING('RoboPack product not found to update'))

            # Show final count
            remaining_products = Product.objects.filter(category=packing_category, is_active=True)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Operation completed. Removed {removed_count} products. '
                    f'Remaining packing robots: {remaining_products.count()}'
                )
            )

            # List remaining products
            for product in remaining_products:
                self.stdout.write(f'  - {product.name}')

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating packing robots: {str(e)}')
            ) 