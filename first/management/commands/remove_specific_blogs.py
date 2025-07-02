from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Remove specific blog posts'

    def handle(self, *args, **options):
        try:
            # List of blog titles to remove
            blog_titles = [
                "Revolutionizing Quality Control",
                "Sustainable Agriculture Through Smart Technology",
                "From Farm to Table: Improving Market Access for Small Farmers"
            ]
            
            # Delete each blog post
            total_deleted = 0
            for title in blog_titles:
                try:
                    blog = BlogPost.objects.get(title=title)
                    blog.delete()
                    total_deleted += 1
                    self.stdout.write(self.style.SUCCESS(f'Successfully deleted blog: {title}'))
                except BlogPost.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Blog not found: {title}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error deleting blog "{title}": {str(e)}'))
            
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {total_deleted} blog posts'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}')) 