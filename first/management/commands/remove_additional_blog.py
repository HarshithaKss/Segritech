from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Remove additional blog post'

    def handle(self, *args, **options):
        try:
            # Blog title to remove
            blog_title = "AI-Powered Fruit Grading: Revolutionizing Quality Control"
            
            try:
                blog = BlogPost.objects.get(title=blog_title)
                blog.delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted blog: {blog_title}'))
            except BlogPost.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Blog not found: {blog_title}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error deleting blog "{blog_title}": {str(e)}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}')) 