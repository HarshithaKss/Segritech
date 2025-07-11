from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Updates author name from "Dr. Hetendra Singh" to "Hetendra Singh" in all blog posts'

    def handle(self, *args, **options):
        # Update all blog posts with the old author name
        updated_count = BlogPost.objects.filter(author_name__contains='Dr. Hetendra Singh').update(
            author_name='Hetendra Singh'
        )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully updated {updated_count} blog posts')
        ) 