import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from first.models import ProductCategory, Product

class Command(BaseCommand):
    help = 'Add enhanced sample products for all categories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating enhanced sample products...'))
        
        # Clear existing products to avoid conflicts
        Product.objects.all().delete()
        
        # Enhanced products data with realistic specifications
        products_data = [
            # Size Graders
            {
                'category': 'Size Graders',
                'name': 'Segritech Apple Size Grading Machine',
                'slug': 'apple-size-grader',
                'short_description': 'Compact apple grading machine with roller-based sorting system. Perfect for farms and mandis with 200-250 box/day capacity.',
                'detailed_description': '''The Segritech Apple Size Grading Machine is a compact and efficient agricultural machine designed for small to medium-scale apple producers. With a robust roller-based grading mechanism, this model provides high accuracy in size grading, ensuring better pricing and packaging for apple growers and aggregators.

Features a durable construction with food-grade materials and integrated cleaning system, making it perfect for farm and mandi operations with 200-250 box/day capacity.''',
                'price_range': 'Contact for Pricing',
                'key_features': json.dumps([
                    'Roller-based size grading system',
                    'Integrated cleaning & drying section',
                    'Food-grade materials (FDA-compliant)',
                    '6-grade output capacity',
                    'Portable design with wheels',
                    'Built for Indian conditions'
                ]),
                'specifications': json.dumps({
                    'Capacity': '200-250 box per day',
                    'Grading Output': '6 Grades',
                    'Dimensions': '10 ft (L) x 4 ft (W) x 4 ft (H)',
                    'Power': '1.5 kW, Single/3 Phase',
                    'Material': 'Stainless Steel, Food-grade Nylon',
                    'Features': 'Cleaning & Grading, Portable Design'
                }),
                'applications': json.dumps([
                    'Small to medium farms',
                    'Fruit packhouses',
                    'Agricultural cooperatives'
                ]),
                'benefits': json.dumps([
                    'Better market pricing',
                    'Reduced labor costs',
                    'Consistent grading quality',
                    'Portable and easy to use'
                ]),
                'lead_time': '',
                'is_featured': True,
                'is_active': True,
                'meta_title': 'Segritech Apple Size Grading Machine | SAGM-200',
                'meta_description': 'Made in India apple grading machine with integrated cleaning system. Perfect for farm and mandi operations with 200-250 box/day capacity.'
            },
            {
                'category': 'Size Graders',
                'name': 'Orange Grader',
                'short_description': 'Compact size grader perfect for oranges with reliable performance.',
                'detailed_description': '''The Segritech Orange Grading Machine is specifically designed for orange grading operations, offering precision sizing in a space-efficient design. Built for Indian agricultural operations, this compact machine delivers reliable performance for cooperative societies and small processing units.

Features advanced mechanical sorting technology optimized for orange characteristics, ensuring consistent size classification while maintaining fruit quality.''',
                'price_range': '₹25,000 - ₹32,000',
                'key_features': json.dumps([
                    'Compact design for space efficiency',
                    'Processing capacity: 250kg/hour',
                    'Easy maintenance and operation',
                    'Cost-effective solution',
                    'Durable construction',
                    'Low power consumption'
                ]),
                'specifications': json.dumps({
                    'Processing Capacity': '250 kg/hour',
                    'Accuracy': '98.5%',
                    'Power Consumption': '3.0 kW',
                    'Dimensions': '1.8m x 1.2m x 1.5m',
                    'Weight': '450 kg',
                    'Material': 'Mild Steel with coating'
                }),
                'applications': json.dumps([
                    'Small processing units',
                    'Cooperative societies',
                    'Specialty crop grading',
                    'Regional distribution centers'
                ]),
                'benefits': json.dumps([
                    'Lower initial investment',
                    'Space-efficient design',
                    'Reliable performance',
                    'Easy to operate'
                ])
            },
            
            # Quality Graders
            {
                'category': 'Quality Graders',
                'name': 'Segritech Minisort',
                'slug': 'segritech-minisort',
                'short_description': 'The Segritech Minisort is a high-capacity, AI-based sorting machine that processes up to 2 tons per hour. It uses advanced camera vision and smart algorithms to detect size, shape, color, and defects across multiple fruit varieties, ensuring export-grade consistency. Built for Indian farms and packhouses with rugged construction and rapid support.',
                'detailed_description': '''The Segritech Minisort is an advanced AI-powered grading machine designed for high-volume fruit sorting across multiple varieties including pomegranates, apples, oranges, and other round fruits. With the capacity to process up to 2 tons per hour, it grades fruits based on size, shape, color, and skin defects using camera vision and AI synchronization.

Ideal for packhouses, mandis, exporters, and farmer cooperatives, the machine ensures export-grade sorting quality with real-time reporting.''',
                'price_range': 'Contact for Pricing',
                'key_features': json.dumps([
                    'AI-powered defect detection',
                    'Camera vision technology',
                    'Real-time quality analysis',
                    'Export-grade sorting',
                    'High capacity processing',
                    'Robust construction'
                ]),
                'specifications': json.dumps({
                    'Capacity': '2 tons per hour (2000 kg/hour)',
                    'Fruit Types': 'Pomegranates, apples, oranges, citrus fruits, and other round fruits',
                    'Grading Parameters': 'Size, shape, color, and external defects',
                    'Technology': 'AI, camera vision, roller assist, and conveyor sync',
                    'Output Grades': '5 to 6 grades (customizable)',
                    'Construction Material': 'Stainless steel, mild steel, aluminum, and food-grade plastic',
                    'Machine Dimensions': '10 feet length, 5 feet width, 5 feet height',
                    'Power Requirement': '3.5 kW or 5 HP',
                    'Voltage': '440V (3-phase) or 220V (single phase), 50 Hz',
                    'Drive Mechanism': 'Motor and conveyor belt synced with AI',
                    'Feeding Mechanism': 'Vibratory or conveyor-fed',
                    'Mobility': 'Industrial-grade caster wheels'
                }),
                'applications': json.dumps([
                    'Packhouses',
                    'Mandis',
                    'Exporters',
                    'Farmer cooperatives',
                    'Large-scale processors'
                ]),
                'benefits': json.dumps([
                    'Export-grade sorting quality',
                    'High processing capacity',
                    'Real-time quality reporting',
                    'Robust construction',
                    'Customizable grading',
                    'Easy maintenance'
                ]),
                'lead_time': '',
                'is_featured': True,
                'is_available': True,
                'meta_title': 'Segritech Minisort | Advanced AI-Powered Fruit Grading',
                'meta_description': 'Advanced AI-powered multifruit grading machine with 2 ton/hour capacity. Features camera vision, defect detection, and export-grade sorting for pomegranates, apples, oranges and more.'
            },
            
            # Weight Graders
            {
                'category': 'Weight Graders',
                'name': 'PrecisionWeight WG-2500 Density Grader',
                'short_description': 'Ultra-precise weight-based grading system for density sorting and export preparation.',
                'detailed_description': '''The Segritech Weight Grader for Fruits delivers exceptional accuracy in weight-based grading, essential for export markets requiring strict weight specifications. Features advanced load cells and vibration dampening for consistent results.

Our weight grader ensures precise sorting based on weight, making it ideal for export quality standards. The machine's advanced technology and robust construction guarantee reliable performance.''',
                'price_range': '₹45,000 - ₹60,000',
                'key_features': json.dumps([
                    'Precision weighing ±0.1g accuracy',
                    'Density-based separation',
                    'Export quality standards compliance',
                    'Multiple weight categories',
                    'Vibration dampening system',
                    'Digital weight display'
                ]),
                'specifications': json.dumps({
                    'Processing Capacity': '300 kg/hour',
                    'Weighing Accuracy': '±0.1g',
                    'Weight Range': '0.1g - 50g per grain',
                    'Power Consumption': '4.5 kW',
                    'Dimensions': '2.2m x 1.6m x 1.8m',
                    'Weight': '720 kg'
                }),
                'applications': json.dumps([
                    'Export preparation facilities',
                    'Premium seed processing',
                    'Quality certification labs',
                    'High-value crop sorting'
                ]),
                'benefits': json.dumps([
                    'Access to premium export markets',
                    'Consistent weight specifications',
                    'Higher selling prices',
                    'Quality certification compliance'
                ])
            },
            
            # Cleaning Machines
            {
                'category': 'Cleaning Machines',
                'name': 'AirClean AC-4000 Multi-Stage Cleaner',
                'short_description': 'Comprehensive cleaning system with air separation, screening, and dust removal.',
                'detailed_description': '''Segriwax™ is a next-generation fruit cleaning and waxing machine tailored for India's decentralized post-harvest ecosystem. Designed for efficiency, affordability, and mobility, Segriwax brings industrial grade performance into a compact, field-deployable solution.

Whether you're a farmer looking to enhance shelf life, or an exporter aiming for retail-grade presentation — Segriwax delivers the finish your produce deserves.''',
                'price_range': '₹35,000 - ₹45,000',
                'key_features': json.dumps([
                    'Multi-stage cleaning process',
                    'Air separation technology',
                    'Dust collection system',
                    'Food-grade stainless steel',
                    'Adjustable air flow',
                    'Easy maintenance access'
                ]),
                'specifications': json.dumps({
                    'Processing Capacity': '800 kg/hour',
                    'Cleaning Efficiency': '99.9%',
                    'Dust Collection': '95% efficiency',
                    'Power Consumption': '7.5 kW',
                    'Dimensions': '3.5m x 2.5m x 3.0m',
                    'Weight': '1100 kg'
                }),
                'applications': json.dumps([
                    'Grain processing mills',
                    'Food processing facilities',
                    'Seed cleaning operations',
                    'Commercial grain elevators'
                ]),
                'benefits': json.dumps([
                    'Food safety compliance',
                    'Improved shelf life',
                    'Better processing efficiency',
                    'Reduced contamination'
                ])
            },
            {
                'category': 'Cleaning Machines',
                'name': 'EcoClean EC-2000 Compact Cleaner',
                'short_description': 'Energy-efficient compact cleaner for small to medium operations.',
                'detailed_description': 'The EcoClean EC-2000 offers effective cleaning in a compact, energy-efficient design. Perfect for smaller operations while maintaining high cleaning standards.',
                'price_range': '₹18,000 - ₹28,000',
                'key_features': json.dumps([
                    'Compact and efficient design',
                    'Low power consumption',
                    'Easy operation',
                    'Minimal maintenance',
                    'Cost-effective solution',
                    'Reliable performance'
                ]),
                'specifications': json.dumps({
                    'Processing Capacity': '400 kg/hour',
                    'Cleaning Efficiency': '98.5%',
                    'Power Consumption': '3.5 kW',
                    'Dimensions': '2.0m x 1.5m x 2.0m',
                    'Weight': '450 kg'
                }),
                'applications': json.dumps([
                    'Small grain mills',
                    'Farm cooperatives',
                    'Regional processing centers',
                    'Specialty crop cleaning'
                ]),
                'benefits': json.dumps([
                    'Lower operating costs',
                    'Space-efficient design',
                    'Easy to maintain',
                    'Suitable for small operations'
                ])
            },
            
            # Packing Robots
            {
                'category': 'Packing Robots',
                'name': 'RoboPack RP-5000 Automated Packaging System',
                'short_description': 'Fully automated packaging robot with precision weighing and multi-format capability.',
                'detailed_description': '''SegriPack is Segritech's flagship automated packaging solution designed specifically for graded fresh produce. This intelligent robotic system combines precision handling with smart weighing technology to deliver consistent, retail-ready packaging.

Built for Indian agricultural operations, SegriPack offers the perfect balance of automation, reliability, and cost-effectiveness. Whether you're packaging pomegranates, apples, citrus fruits, or other fresh produce, SegriPack ensures professional presentation while reducing labor dependency.''',
                'price_range': '₹1,10,000 - ₹1,35,000',
                'key_features': json.dumps([
                    'Robotic arm automation',
                    'Precision weighing system',
                    'Multi-format packaging',
                    'Bag detection and positioning',
                    'Quality control sensors',
                    'Production monitoring dashboard'
                ]),
                'specifications': json.dumps({
                    'Packaging Speed': '200 bags/hour',
                    'Weight Range': '1kg - 50kg',
                    'Accuracy': '±5g',
                    'Power Consumption': '12 kW',
                    'Dimensions': '4.0m x 3.0m x 2.5m',
                    'Weight': '1800 kg'
                }),
                'applications': json.dumps([
                    'Large processing facilities',
                    'Export packaging centers',
                    'Commercial grain operations',
                    'High-volume packaging lines'
                ]),
                'benefits': json.dumps([
                    'Reduced labor costs',
                    'Consistent packaging quality',
                    'Increased throughput',
                    'Reduced packaging errors'
                ])
            },
            {
                'category': 'Packing Robots',
                'name': 'FlexiPack FP-3000 Semi-Automated Packer',
                'short_description': 'Semi-automated packaging solution with operator assistance for medium-scale operations.',
                'detailed_description': 'The FlexiPack FP-3000 combines automation with operator control, offering flexibility and cost-effectiveness for medium-scale packaging operations.',
                'price_range': '₹60,000 - ₹75,000',
                'key_features': json.dumps([
                    'Semi-automated operation',
                    'Operator-assisted control',
                    'Flexible packaging options',
                    'Easy setup and changeover',
                    'Cost-effective solution',
                    'User-friendly interface'
                ]),
                'specifications': json.dumps({
                    'Packaging Speed': '120 bags/hour',
                    'Weight Range': '1kg - 25kg',
                    'Accuracy': '±10g',
                    'Power Consumption': '6 kW',
                    'Dimensions': '3.0m x 2.0m x 2.0m',
                    'Weight': '800 kg'
                }),
                'applications': json.dumps([
                    'Medium processing facilities',
                    'Regional distribution centers',
                    'Specialty product packaging',
                    'Flexible packaging lines'
                ]),
                'benefits': json.dumps([
                    'Lower initial investment',
                    'Operational flexibility',
                    'Easy to learn and operate',
                    'Suitable for varied products'
                ])
            }
        ]
        
        products_created = 0
        for product_data in products_data:
            try:
                category = ProductCategory.objects.get(name=product_data['category'])
                
                # Create slug from name
                slug = slugify(product_data['name'])
                
                # Check if product with this slug already exists
                if Product.objects.filter(slug=slug).exists():
                    # Append number to make it unique
                    counter = 1
                    while Product.objects.filter(slug=f"{slug}-{counter}").exists():
                        counter += 1
                    slug = f"{slug}-{counter}"
                
                product = Product.objects.create(
                    category=category,
                    name=product_data['name'],
                    slug=slug,
                    short_description=product_data['short_description'],
                    detailed_description=product_data['detailed_description'],
                    price_range=product_data['price_range'],
                    key_features=product_data['key_features'],
                    specifications=product_data['specifications'],
                    applications=product_data['applications'],
                    benefits=product_data['benefits'],
                    is_featured=True,
                    is_available=True
                )
                
                products_created += 1
                self.stdout.write(f"✓ Created product: {product.name}")
                
            except ProductCategory.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Category '{product_data['category']}' not found. Run setup_categories first.")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating product '{product_data['name']}': {str(e)}")
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {products_created} enhanced products!')
        ) 