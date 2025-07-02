"""
Django management command to set up all necessary data in the database.
This command runs all required commands in sequence to populate the database with categories,
products, blogs, and other content. Designed to be run after deploying to a new environment.
"""

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db import transaction
from django.conf import settings
import os


class Command(BaseCommand):
    help = 'Set up all necessary data in the database by running all required commands in sequence'

    def run_command_safely(self, command_name, step_description):
        """Run a command and handle any errors gracefully"""
        try:
            call_command(command_name)
            return True
        except Exception as e:
            self.stdout.write(
                self.style.WARNING(f'\nWarning: Error in {step_description} ({command_name}): {str(e)}')
            )
            return False

    def handle(self, *args, **options):
        errors = []
        
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

            self.stdout.write('Starting complete database setup...')
            
            # Step 1: Set up basic categories
            self.stdout.write('\n1. Setting up product categories...')
            if not self.run_command_safely('setup_categories', 'setting up categories'):
                errors.append('Failed to set up categories')
            
            # Step 2: Add products
            self.stdout.write('\n2. Adding enhanced products...')
            if not self.run_command_safely('add_enhanced_products', 'adding products'):
                errors.append('Failed to add enhanced products')
            
            # Step 3: Update specific products
            self.stdout.write('\n3. Updating specific products...')
            commands = [
                ('add_segriwax_machine', 'adding Segriwax machine'),
                ('cleanup_cleaning_machines', 'cleaning up machines'),
                ('update_orange_grader_name', 'updating orange grader'),
                ('update_packing_robots', 'updating packing robots'),
                ('update_product_brochures', 'updating product brochures')
            ]
            for cmd, desc in commands:
                if not self.run_command_safely(cmd, desc):
                    errors.append(f'Failed to {desc}')
            
            # Step 4: Set up brochures
            self.stdout.write('\n4. Setting up brochure files...')
            if not self.run_command_safely('setup_brochures', 'setting up brochures'):
                errors.append('Failed to set up brochures')
            
            # Step 5: Add blogs and content
            self.stdout.write('\n5. Setting up blog content...')
            if not self.run_command_safely('add_featured_blogs', 'adding blogs'):
                errors.append('Failed to add featured blogs')
            
            # Step 6: Add testimonials and other content
            self.stdout.write('\n6. Adding testimonials and other content...')
            if not self.run_command_safely('add_sample_testimonials', 'adding testimonials'):
                errors.append('Failed to add testimonials')
            if not self.run_command_safely('add_sample_contacts', 'adding contacts'):
                errors.append('Failed to add contacts')
            if not self.run_command_safely('add_sample_newsletter_subscribers', 'adding subscribers'):
                errors.append('Failed to add newsletter subscribers')
            
            # Final status report
            if errors:
                self.stdout.write(
                    self.style.WARNING(
                        '\nSetup completed with some warnings:'
                        f'\n- {"- ".join(errors)}'
                        '\nSome features may not work as expected.'
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('\nSuccessfully set up all data in the database!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'\nCritical error during setup: {str(e)}')
            )
            raise CommandError('Setup failed due to critical error') 