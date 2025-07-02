from django.core.management.base import BaseCommand
from first.models import NewsletterSubscriber
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Add sample newsletter subscribers'

    def handle(self, *args, **kwargs):
        subscribers = [
            {
                'email': 'farmer.kumar@example.com',
                'subscribed_at': timezone.now() - timedelta(days=30),
                'is_active': True
            },
            {
                'email': 'agritech.news@example.com',
                'subscribed_at': timezone.now() - timedelta(days=25),
                'is_active': True
            },
            {
                'email': 'fruit.exports@example.com',
                'subscribed_at': timezone.now() - timedelta(days=20),
                'is_active': True
            },
            {
                'email': 'research.agri@example.com',
                'subscribed_at': timezone.now() - timedelta(days=15),
                'is_active': True
            },
            {
                'email': 'tech.farmer@example.com',
                'subscribed_at': timezone.now() - timedelta(days=10),
                'is_active': True
            },
            {
                'email': 'organic.grower@example.com',
                'subscribed_at': timezone.now() - timedelta(days=5),
                'is_active': True
            },
            {
                'email': 'smart.agriculture@example.com',
                'subscribed_at': timezone.now() - timedelta(days=3),
                'is_active': True
            },
            {
                'email': 'unsubscribed.user@example.com',
                'subscribed_at': timezone.now() - timedelta(days=45),
                'is_active': False
            }
        ]

        for subscriber_data in subscribers:
            NewsletterSubscriber.objects.create(**subscriber_data)

        self.stdout.write(self.style.SUCCESS('Successfully added sample newsletter subscribers')) 