from django.core.management.base import BaseCommand
from first.models import ProductInquiry, Product
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Add sample product inquiries'

    def handle(self, *args, **kwargs):
        # Get some products to reference
        try:
            products = Product.objects.filter(is_active=True)[:3]
            if not products:
                self.stdout.write(self.style.WARNING('No active products found. Please add products first.'))
                return
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('No products exist. Please add products first.'))
            return

        inquiries = [
            {
                'name': 'Ramesh Patil',
                'email': 'ramesh.p@example.com',
                'phone': '+91 9876543210',
                'company': 'Patil Farms',
                'inquiry_type': 'demo',
                'message': 'We have a large mango farm and interested in your grading machine. Would like to see a demo and understand the capacity.',
                'created_at': timezone.now() - timedelta(days=3),
                'is_responded': True
            },
            {
                'name': 'Li Wei',
                'email': 'li.wei@example.com',
                'phone': '+86 13812345678',
                'company': 'Golden Fruits Trading',
                'inquiry_type': 'bulk_order',
                'message': 'Looking to place bulk order for 10 machines. Need details about bulk pricing, shipping to China, and installation support.',
                'created_at': timezone.now() - timedelta(days=2),
                'is_responded': False
            },
            {
                'name': 'John Anderson',
                'email': 'john.a@example.com',
                'phone': '+1 987-654-3210',
                'company': 'Fresh Pack Solutions',
                'inquiry_type': 'specs',
                'message': 'Need detailed technical specifications for your apple grading machine. Particularly interested in throughput capacity and sorting accuracy.',
                'created_at': timezone.now() - timedelta(days=1),
                'is_responded': False
            },
            {
                'name': 'Priya Mehta',
                'email': 'priya.m@example.com',
                'phone': '+91 8765432109',
                'company': 'Mehta Exports',
                'inquiry_type': 'customization',
                'message': 'We need a custom solution for pomegranate grading. Can your machines be modified for this specific fruit?',
                'created_at': timezone.now() - timedelta(hours=12),
                'is_responded': False
            },
            {
                'name': 'Ahmed Hassan',
                'email': 'ahmed.h@example.com',
                'phone': '+20 109876543',
                'company': 'Egyptian Fruits Co',
                'inquiry_type': 'partnership',
                'message': 'Interested in becoming your distributor in Egypt. We have strong connections in the agricultural sector.',
                'created_at': timezone.now() - timedelta(hours=6),
                'is_responded': False
            }
        ]

        # Distribute inquiries across available products
        for i, inquiry_data in enumerate(inquiries):
            product = products[i % len(products)]
            ProductInquiry.objects.create(
                product=product,
                **inquiry_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample product inquiries')) 