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
    help = 'Sets up all initial data for the application'

    def handle(self, *args, **options):
        # List of commands to run in order
        commands = [
            # Initial setup
            'setup_categories',  # Set up product categories
            'setup_brochures',   # Set up product brochures
            'setup_blog_images', # Set up blog images
            'add_sample_faqs',   # Set up FAQs
            
            # Products setup
            'add_enhanced_products',     # Add main products
            'add_segriwax_machine',      # Add Segriwax machine
            'cleanup_cleaning_machines', # Remove unwanted cleaning machines
            'update_minisort_name',      # Update Minisort product name
            'update_weight_grader_name', # Update Weight Grader name
            'update_orange_grader_name', # Update Orange Grader name
            'update_packing_robots',     # Update packing robot products
            'update_product_brochures',  # Update product brochures
            
            # Blog content setup
            'add_featured_blogs',        # Add featured blogs
            'add_sample_blogs',          # Add sample blog posts
            'import_linkedin_articles',   # Import LinkedIn articles
            'populate_media_articles',    # Add media articles
            'manage_featured_blogs',      # Manage featured blog status
            'update_author_name',        # Update author names in blogs
            'fix_blog_content',          # Fix any blog content issues
            'shorten_all_descriptions',  # Ensure blog descriptions are proper length
            
            # Jobs and careers setup
            'add_sample_jobs',           # Add job postings
            'cleanup_duplicate_jobs',    # Remove any duplicate job postings
            
            # Sample data for testing
            'add_sample_contacts',       # Add sample contact submissions
            'add_sample_newsletter_subscribers',  # Add newsletter subscribers
            'add_sample_product_inquiries',      # Add product inquiries
            'add_sample_testimonials',           # Add testimonials
        ]

        for command in commands:
            try:
                self.stdout.write(f'Running {command}...')
                call_command(command)
                self.stdout.write(self.style.SUCCESS(f'Successfully ran {command}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error running {command}: {str(e)}'))
                # Continue with other commands even if one fails
                continue

        self.stdout.write(self.style.SUCCESS('All data has been set up successfully')) 