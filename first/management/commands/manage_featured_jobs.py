from django.core.management.base import BaseCommand
from first.models import JobPosting

class Command(BaseCommand):
    help = 'Manages featured job postings'

    def handle(self, *args, **kwargs):
        # First, unset all featured flags
        JobPosting.objects.all().update(is_featured=False)
        
        # Define the titles of jobs that should be featured
        featured_job_titles = [
            "Mechanical Engineer",  # Core engineering role
            "Mechatronics Internship",  # Entry level opportunity
        ]
        
        # Set featured flag for specified jobs
        featured_count = 0
        for title in featured_job_titles:
            try:
                job = JobPosting.objects.get(title=title)
                job.is_featured = True
                job.save()
                featured_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully featured job: {title}'))
            except JobPosting.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Job not found: {title}'))
            except JobPosting.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(f'Multiple jobs found with title: {title}'))
        
        self.stdout.write(self.style.SUCCESS(f'Featured {featured_count} jobs')) 