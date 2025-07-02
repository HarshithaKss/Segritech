from django.core.management.base import BaseCommand
from first.models import Contact
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Add sample contact inquiries'

    def handle(self, *args, **kwargs):
        contacts = [
            {
                'name': 'Vikram Singh',
                'email': 'vikram.singh@example.com',
                'phone': '+91 9876543210',
                'company': 'Fresh Fruits Co.',
                'inquiry_type': 'product',
                'subject': 'Apple Grading Machine Inquiry',
                'message': 'We are interested in your apple grading machine. We process about 5 tons of apples daily and looking for an automated solution. Please share detailed specifications and pricing.',
                'created_at': timezone.now() - timedelta(days=2),
                'is_read': True
            },
            {
                'name': 'Sarah Johnson',
                'email': 'sarah.j@example.com',
                'phone': '+1 234-567-8900',
                'company': 'Global Agri Exports',
                'inquiry_type': 'partnership',
                'subject': 'Distribution Partnership Opportunity',
                'message': 'We are a leading agricultural equipment distributor in the US and interested in partnering with SegriTech. Would like to discuss distribution rights for North America.',
                'created_at': timezone.now() - timedelta(days=1),
                'is_read': False
            },
            {
                'name': 'Rajesh Kumar',
                'email': 'rajesh.k@example.com',
                'phone': '+91 8765432109',
                'company': 'Kumar Orchards',
                'inquiry_type': 'demo',
                'subject': 'Request for Live Demo',
                'message': 'Interested in seeing your grading machine in action. We have an orange farm in Maharashtra. Can you arrange a demo at a nearby location?',
                'created_at': timezone.now() - timedelta(hours=12),
                'is_read': False
            },
            {
                'name': 'Maria Garcia',
                'email': 'maria.g@example.com',
                'phone': '+34 612345678',
                'company': 'Spanish Fruits SL',
                'inquiry_type': 'pricing',
                'subject': 'Pricing for Bulk Order',
                'message': 'Looking to upgrade our entire sorting facility. Need pricing for 5 machines with installation and training. Also interested in annual maintenance contract.',
                'created_at': timezone.now() - timedelta(hours=6),
                'is_read': False
            },
            {
                'name': 'Dr. Amit Shah',
                'email': 'amit.shah@example.com',
                'phone': '+91 7654321098',
                'company': 'Agri Research Institute',
                'inquiry_type': 'support',
                'subject': 'Technical Documentation Request',
                'message': 'Working on a research paper about AI in agricultural automation. Would like to know if you can share any technical documentation about your AI grading algorithms.',
                'created_at': timezone.now() - timedelta(hours=2),
                'is_read': False
            }
        ]

        for contact_data in contacts:
            Contact.objects.create(**contact_data)

        self.stdout.write(self.style.SUCCESS('Successfully added sample contact inquiries')) 