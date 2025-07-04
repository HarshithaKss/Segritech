"""
Django management command to set up all testimonial data.
This includes creating testimonials with proper photos and ratings.
"""

from django.core.management.base import BaseCommand
from django.core.files import File
from first.models import Testimonial
from django.conf import settings
import os
import shutil

class Command(BaseCommand):
    help = 'Set up all testimonial data including photos'

    def handle(self, *args, **options):
        self.stdout.write('Setting up testimonials...')

        # Define testimonial data
        testimonials = [
            {
                'name': 'Rajesh Kumar',
                'role': 'farmer',
                'company_or_location': 'Organic Farm Collective',
                'country': 'India',
                'quote': 'सेग्रीटेक मशीन से हमारी फसल की गुणवत्ता में 45% का सुधार हुआ है। यह हमारे किसान समुदाय के लिए एक बेहतरीन निवेश साबित हुआ!',
                'impact_metric': '45% Quality Improvement',
                'impact_icon': 'fas fa-chart-line',
                'is_featured': True,
                'display_order': 1,
                'rating': 4.8,
                'photo_src': 'member-img2.png'
            },
            {
                'name': 'Priya Sharma',
                'role': 'export_manager',
                'company_or_location': 'Fresh Fruits Export Ltd',
                'country': 'India',
                'quote': 'Since implementing SegriTech\'s quality grading system, our export rejection rates have dropped by 35%. The consistency and accuracy are remarkable.',
                'impact_metric': '35% Lower Rejections',
                'impact_icon': 'fas fa-chart-line',
                'is_featured': True,
                'display_order': 2,
                'rating': 5.0,
                'photo_src': 'member-img1.png'
            },
            {
                'name': 'Maria Santos',
                'role': 'trader',
                'company_or_location': 'Agricultural Trading Company',
                'country': 'Brazil',
                'quote': "Export quality improved dramatically. Our international clients are impressed with the consistent grading!",
                'impact_metric': '60% Efficiency Boost',
                'impact_icon': 'fas fa-rocket',
                'display_order': 3,
                'rating': 4.7,
                'photo_src': 'member-img3.png'
            },
            {
                'name': 'Dr. Amit Patel',
                'role': 'researcher',
                'company_or_location': 'Agricultural Research Institute',
                'country': 'India',
                'quote': 'The AI capabilities of SegriTech\'s machines are impressive. Their system has helped us collect valuable data on crop quality patterns across different seasons.',
                'impact_metric': '500+ Data Points Daily',
                'impact_icon': 'fas fa-database',
                'is_featured': False,
                'display_order': 4,
                'rating': 4.9,
                'photo_src': 'member-img4.png'
            },
            {
                'name': 'Meera Reddy',
                'role': 'cooperative_manager',
                'company_or_location': 'Farmers\' Cooperative Society',
                'country': 'India',
                'quote': 'Our small farmers have seen a 25% increase in market value for their produce after implementing SegriTech\'s grading solutions. The return on investment has been excellent.',
                'impact_metric': '25% Value Increase',
                'impact_icon': 'fas fa-rupee-sign',
                'is_featured': True,
                'display_order': 5,
                'rating': 4.7,
                'photo_src': 'member-img5.png'
            }
        ]

        # Create testimonials directory if it doesn't exist
        testimonials_dir = os.path.join(settings.MEDIA_ROOT, 'testimonials')
        if not os.path.exists(testimonials_dir):
            os.makedirs(testimonials_dir)

        # Process each testimonial
        for testimonial_data in testimonials:
            # Get the photo source path
            photo_src = testimonial_data.pop('photo_src')
            photo_path = os.path.join(settings.STATIC_ROOT, 'images', photo_src)
            
            # Create or update testimonial
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                defaults=testimonial_data
            )

            # Copy photo to media directory
            if os.path.exists(photo_path):
                photo_dest = os.path.join(testimonials_dir, photo_src)
                shutil.copy2(photo_path, photo_dest)
                
                # Update testimonial photo field
                with open(photo_dest, 'rb') as f:
                    testimonial.photo.save(photo_src, File(f), save=True)

            if created:
                self.stdout.write(f'Created testimonial: {testimonial.name}')
            else:
                # Update existing testimonial
                for key, value in testimonial_data.items():
                    setattr(testimonial, key, value)
                testimonial.save()
                self.stdout.write(f'Updated testimonial: {testimonial.name}')

        self.stdout.write(self.style.SUCCESS('Successfully set up all testimonials!')) 