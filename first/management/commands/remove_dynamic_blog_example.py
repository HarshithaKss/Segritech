from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Remove the Dynamic Blog Post Example about AI-Powered Agricultural Technology'

    def handle(self, *args, **options):
        try:
            # Try to find and delete the blog post
            blog = BlogPost.objects.filter(
                title__icontains='Dynamic Blog Post Example',
                title__icontains='AI-Powered Agricultural Technology'
            ).first()
            
            if blog:
                blog.delete()
                self.stdout.write(
                    self.style.SUCCESS('Successfully removed the dynamic blog example post')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Dynamic blog example post not found - nothing to remove')
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error removing dynamic blog example post: {str(e)}')
            ) 