from django.core.management.base import BaseCommand
from first.models import ProductCategory

class Command(BaseCommand):
    help = 'Set up the 5 product categories for SegriTech'
    
    def handle(self, *args, **options):
        categories_data = [
            {
                'name': 'Size Graders',
                'slug': 'size-graders',
                'category_type': 'size_graders',
                'short_description': 'Precision size-based sorting machines for uniform crop grading',
                'description': 'Our size graders use advanced optical and mechanical sorting technology to classify crops based on their physical dimensions. Perfect for ensuring uniform quality and meeting specific market requirements.',
                'icon': 'fas fa-ruler-horizontal',
                'display_order': 1
            },
            {
                'name': 'Quality Graders',
                'slug': 'quality-graders', 
                'category_type': 'quality_graders',
                'short_description': 'AI-powered quality assessment and classification systems',
                'description': 'Intelligent quality grading systems that use computer vision and AI to assess crop quality, color, defects, and overall grade. Ensures consistent quality standards across your entire harvest.',
                'icon': 'fas fa-star',
                'display_order': 2
            },
            {
                'name': 'Weight Graders',
                'slug': 'weight-graders',
                'category_type': 'weight_graders', 
                'short_description': 'High-precision weight-based sorting and classification',
                'description': 'Accurate weight-based grading systems that sort crops into precise weight categories. Essential for premium packaging and meeting specific weight requirements for different market segments.',
                'icon': 'fas fa-weight',
                'display_order': 3
            },
            {
                'name': 'Cleaning Machines',
                'slug': 'cleaning-machines',
                'category_type': 'cleaning_machines',
                'short_description': 'Advanced cleaning and debris removal systems',
                'description': 'Comprehensive cleaning solutions that remove impurities, foreign materials, and damaged crops. Multi-stage cleaning process ensures your crops meet the highest hygiene and quality standards.',
                'icon': 'fas fa-apple-alt',
                'display_order': 4
            },
            {
                'name': 'Packing Robots',
                'slug': 'packing-robots',
                'category_type': 'packing_robots',
                'short_description': 'Automated robotic packaging and handling solutions',
                'description': 'State-of-the-art robotic systems for automated packaging, handling, and palletizing. Increase efficiency while reducing labor costs and ensuring consistent packaging quality.',
                'icon': 'fas fa-robot',
                'display_order': 5
            }
        ]
        
        created_count = 0
        updated_count = 0
        
        for category_data in categories_data:
            category, created = ProductCategory.objects.update_or_create(
                category_type=category_data['category_type'],
                defaults={
                    'name': category_data['name'],
                    'slug': category_data['slug'],
                    'short_description': category_data['short_description'],
                    'description': category_data['description'],
                    'icon': category_data['icon'],
                    'display_order': category_data['display_order'],
                    'is_active': True
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated category: {category.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSummary: {created_count} categories created, {updated_count} categories updated'
            )
        ) 