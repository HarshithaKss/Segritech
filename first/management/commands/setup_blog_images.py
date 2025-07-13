from django.core.management.base import BaseCommand
from django.core.files import File
from first.models import BlogPost
from django.conf import settings
import os
import shutil

class Command(BaseCommand):
    help = 'Set up featured images for blog posts'

    def handle(self, *args, **options):
        # First, clear any existing featured images
        BlogPost.objects.all().update(featured_image='')
        
        # Dictionary mapping blog titles to their respective images
        blog_images = {
            'List of Countries Importing Fruit & Vegetables from India': 'List_of_countries.png',
            'Export Fruits and Vegetables to Bangladesh': 'Export_fruit.png',
            'Groundbreaking Robots in Agriculture': 'Ground.png'
        }

        # Path to the source images - look in static directory first, then staticfiles
        source_image_dir = os.path.join(settings.BASE_DIR, 'static', 'images', 'blog')
        if not os.path.exists(source_image_dir):
            source_image_dir = os.path.join(settings.STATIC_ROOT, 'images', 'blog')
            if not os.path.exists(source_image_dir):
                self.stdout.write(self.style.ERROR(f'Blog images directory not found at {source_image_dir}'))
                return

        # Create media/blog_images directory if it doesn't exist
        media_dir = os.path.join(settings.MEDIA_ROOT, 'blog_images')
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)

        # Set up images for each blog
        for title, image_name in blog_images.items():
            try:
                blog = BlogPost.objects.get(title=title)
                source_path = os.path.join(source_image_dir, image_name)
                
                self.stdout.write(f'Processing blog: {title}')
                self.stdout.write(f'Looking for image: {source_path}')
                
                if os.path.exists(source_path):
                    # Create destination path
                    dest_path = os.path.join(media_dir, image_name)
                    
                    # Copy the image to media directory
                    shutil.copy2(source_path, dest_path)
                    
                    # Set the featured image
                    with open(dest_path, 'rb') as img_file:
                        blog.featured_image.save(image_name, File(img_file), save=True)
                    
                    # Verify the image was set
                    blog.refresh_from_db()
                    if blog.featured_image:
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Successfully set featured image for blog: {title}')
                        )
                    else:
                        self.stdout.write(
                            self.style.ERROR(f'✗ Failed to set image for blog: {title}')
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'✗ Image not found: {source_path}')
                    )
            except BlogPost.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'✗ Blog not found: {title}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error setting image for {title}: {str(e)}')
                ) 