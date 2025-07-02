"""
Django management command to set up all necessary data in the database.
This command runs all required commands in sequence to populate the database with categories,
products, blogs, and other content. Designed to be run after deploying to a new environment.
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Set up all necessary data in the database by running all required commands in sequence'

    def handle(self, *args, **options):
        try:
            # Ensure media directory exists
            media_root = settings.MEDIA_ROOT
            if not os.path.exists(media_root):
                os.makedirs(media_root)
                self.stdout.write(f'Created media directory at {media_root}')

            # Ensure static directory exists
            static_root = settings.STATIC_ROOT
            if not os.path.exists(static_root):
                os.makedirs(static_root)
                self.stdout.write(f'Created static directory at {static_root}')

            with transaction.atomic():
                self.stdout.write('Starting complete database setup...')
                
                # Step 1: Set up basic categories
                self.stdout.write('\n1. Setting up product categories...')
                call_command('setup_categories')
                
                # Step 2: Add products
                self.stdout.write('\n2. Adding enhanced products...')
                call_command('add_enhanced_products')
                
                # Step 3: Update specific products
                self.stdout.write('\n3. Updating specific products...')
                call_command('add_segriwax_machine')
                call_command('cleanup_cleaning_machines')
                call_command('update_orange_grader_name')
                call_command('update_packing_robots')
                call_command('update_product_brochures')
                
                # Step 4: Set up brochures
                self.stdout.write('\n4. Setting up brochure files...')
                call_command('setup_brochures')
                
                # Step 5: Add blogs and content
                self.stdout.write('\n5. Setting up blog content...')
                call_command('add_featured_blogs')
                
                # Step 6: Add testimonials and other content
                self.stdout.write('\n6. Adding testimonials and other content...')
                call_command('add_sample_testimonials')
                call_command('add_sample_contacts')
                call_command('add_sample_newsletter_subscribers')
                
                self.stdout.write(
                    self.style.SUCCESS('\nSuccessfully set up all data in the database!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'\nError setting up data: {str(e)}')
            )
            raise e 