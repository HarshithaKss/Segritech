from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import ProductCategory, Product

class Command(BaseCommand):
    help = 'Add sample products to test the functionality'

    def handle(self, *args, **options):
        # Get the categories
        size_graders = ProductCategory.objects.filter(category_type='size_graders').first()
        quality_graders = ProductCategory.objects.filter(category_type='quality_graders').first()
        weight_graders = ProductCategory.objects.filter(category_type='weight_graders').first()
        cleaning_machines = ProductCategory.objects.filter(category_type='cleaning_machines').first()
        packing_robots = ProductCategory.objects.filter(category_type='packing_robots').first()

        if not size_graders:
            self.stdout.write(self.style.ERROR('Categories not found. Please run setup_categories first.'))
            return

        # Sample products data
        products_data = [
            {
                'name': 'Advanced Optical Size Grader SG-2000',
                'category': size_graders,
                'short_description': 'High-precision optical size grading machine for fruits and vegetables.',
                'detailed_description': 'High-precision optical size grading machine for fruits and vegetables with advanced computer vision technology.',
                'key_features': '["High-speed sorting up to 10 tons/hour", "Advanced optical sensors", "User-friendly touch interface", "Minimal waste generation"]',
                'benefits': 'Improved product quality, reduced labor costs, consistent grading standards, increased throughput.',
                'applications': 'Perfect for fruit and vegetable processing facilities, export houses, and large farms.',
                'specifications': '{"capacity": "10 tons/hour", "power": "5 kW", "accuracy": "99.5%"}',
                'price_range': '$50,000 - $75,000',
                'is_featured': True,
                'is_active': True,
            },
            {
                'name': 'Multi-Spectrum Quality Analyzer QG-500',
                'category': quality_graders,
                'short_description': 'Advanced quality grading system using multiple spectrum analysis.',
                'detailed_description': 'Advanced quality grading system using multiple spectrum analysis for detecting defects and quality parameters.',
                'key_features': '["Multi-spectrum analysis", "Real-time quality assessment", "Automatic defect detection", "Data logging and reporting"]',
                'benefits': 'Enhanced quality control, reduced human error, improved product consistency, detailed quality reports.',
                'applications': 'Ideal for quality control in food processing, export grading, and premium product lines.',
                'specifications': '{"sensors": "RGB, NIR, UV", "processing_speed": "5 items/second", "accuracy": "97%"}',
                'price_range': '$80,000 - $120,000',
                'is_featured': True,
                'is_active': True,
            },
            {
                'name': 'Precision Weight Grader WG-1500',
                'category': weight_graders,
                'short_description': 'High-accuracy weight grading machine for precise classification.',
                'detailed_description': 'High-accuracy weight grading machine for precise classification based on weight parameters.',
                'key_features': '["High-precision load cells", "Multi-lane sorting", "Reject handling system", "Statistical reporting"]',
                'benefits': 'Accurate weight classification, improved pack consistency, reduced giveaway, enhanced customer satisfaction.',
                'applications': 'Perfect for packaging lines, portion control, and automated sorting systems.',
                'specifications': '{"accuracy": "±0.1g", "throughput": "150 items/minute", "weight_range": "1g-5kg"}',
                'price_range': '$40,000 - $60,000',
                'is_featured': True,
                'is_active': True,
            },
            {
                'name': 'Industrial Cleaning System IC-3000',
                'category': cleaning_machines,
                'short_description': 'Comprehensive cleaning and washing system for agricultural products.',
                'detailed_description': 'Comprehensive cleaning and washing system for agricultural products with multiple cleaning stages.',
                'key_features': '["Multi-stage cleaning process", "Water recycling system", "Adjustable pressure settings", "Easy maintenance design"]',
                'benefits': 'Superior cleaning efficiency, water conservation, reduced contamination risk, extended product shelf life.',
                'applications': 'Essential for food safety, pre-processing cleaning, and contamination removal.',
                'specifications': '{"water_usage": "50L/hour", "cleaning_stages": "5", "capacity": "2 tons/hour"}',
                'price_range': '$30,000 - $45,000',
                'is_featured': False,
                'is_active': True,
            },
            {
                'name': 'Automated Packing Robot PR-2500',
                'category': packing_robots,
                'short_description': 'Fully automated robotic packing system for agricultural products.',
                'detailed_description': 'Fully automated robotic packing system for various agricultural products with intelligent handling.',
                'key_features': '["6-axis robotic arm", "Vision-guided picking", "Multiple packaging formats", "Safety sensors"]',
                'benefits': 'Reduced labor costs, consistent packing quality, increased productivity, improved workplace safety.',
                'applications': 'Automated packaging lines, high-volume operations, and consistent product presentation.',
                'specifications': '{"reach": "1.5m", "payload": "10kg", "speed": "60 picks/minute", "accuracy": "±1mm"}',
                'price_range': '$100,000 - $150,000',
                'is_featured': True,
                'is_active': True,
            },
        ]

        created_count = 0
        for product_data in products_data:
            # Generate unique slug
            base_slug = slugify(product_data['name'])
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            product_data['slug'] = slug
            
            # Skip main_image field for now since it's required but we don't have actual images
            # Users can add images later through the admin interface
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(f"Created product: {product.name}")
            else:
                self.stdout.write(f"Product already exists: {product.name}")

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample products!')
        ) 