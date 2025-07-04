from django.core.management.base import BaseCommand
from first.models import Testimonial
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add sample testimonials'

    def handle(self, *args, **kwargs):
        testimonials = [
            {
                'name': 'Rajesh Kumar',
                'role': 'farmer',
                'company_or_location': 'Organic Farm Collective',
                'country': 'India',
                'quote': 'The SegriTech grading machine has transformed how we process our apples. We\'ve seen a 40% reduction in sorting time and improved accuracy in quality grading.',
                'impact_metric': '40% Time Reduction',
                'impact_icon': 'fas fa-clock',
                'is_featured': True,
                'display_order': 1
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
                'display_order': 2
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
                'display_order': 3
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
                'display_order': 4
            },
            {
                'name': 'John Smith',
                'role': 'entrepreneur',
                'company_or_location': 'AgriTech Solutions',
                'country': 'United States',
                'quote': 'SegriTech\'s machines are robust and reliable. We\'ve processed over 100 tons of fruits with consistent grading accuracy above 95%.',
                'impact_metric': '95% Accuracy Rate',
                'impact_icon': 'fas fa-check-circle',
                'is_featured': False,
                'display_order': 5
            }
        ]

        for testimonial_data in testimonials:
            Testimonial.objects.create(
                name=testimonial_data['name'],
                role=testimonial_data['role'],
                company_or_location=testimonial_data['company_or_location'],
                country=testimonial_data['country'],
                quote=testimonial_data['quote'],
                impact_metric=testimonial_data['impact_metric'],
                impact_icon=testimonial_data['impact_icon'],
                is_featured=testimonial_data['is_featured'],
                display_order=testimonial_data['display_order'],
                is_active=True
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample testimonials')) 