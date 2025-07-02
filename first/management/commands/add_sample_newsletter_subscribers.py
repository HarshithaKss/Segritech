from django.core.management.base import BaseCommand
from first.models import NewsletterSubscriber
from django.utils import timezone

class Command(BaseCommand):
    help = 'Add sample newsletter subscribers'

    def handle(self, *args, **options):
        subscribers_data = [
            {
                'email': 'farmer@example.com',
                'name': 'John Smith',
                'subscription_date': timezone.now(),
                'is_active': True,
                'subscription_type': 'farmer'
            },
            {
                'email': 'exporter@example.com',
                'name': 'Sarah Johnson',
                'subscription_date': timezone.now(),
                'is_active': True,
                'subscription_type': 'exporter'
            },
            {
                'email': 'distributor@example.com',
                'name': 'Michael Chen',
                'subscription_date': timezone.now(),
                'is_active': True,
                'subscription_type': 'distributor'
            },
            {
                'email': 'processor@example.com',
                'name': 'Emma Davis',
                'subscription_date': timezone.now(),
                'is_active': True,
                'subscription_type': 'processor'
            }
        ]

        created_count = 0
        existing_count = 0

        for subscriber_data in subscribers_data:
            try:
                subscriber, created = NewsletterSubscriber.objects.get_or_create(
                    email=subscriber_data['email'],
                    defaults=subscriber_data
                )
                if created:
                    created_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'Created subscriber: {subscriber.email}')
                    )
                else:
                    existing_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'Subscriber already exists: {subscriber.email}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error processing subscriber {subscriber_data["email"]}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nNewsletter subscribers setup completed:'
                f'\n- Created: {created_count}'
                f'\n- Already existed: {existing_count}'
            )
        ) 