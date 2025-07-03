from django.core.management.base import BaseCommand
from first.models import JobPosting
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate job postings'

    def handle(self, *args, **kwargs):
        # Find duplicate jobs by title
        duplicates = JobPosting.objects.values('title').annotate(
            count=Count('id')
        ).filter(count__gt=1)

        for dup in duplicates:
            title = dup['title']
            # Get all jobs with this title, ordered by creation date
            jobs = JobPosting.objects.filter(title=title).order_by('created_at')
            
            # Keep the oldest job, delete the rest
            oldest_job = jobs.first()
            jobs.exclude(id=oldest_job.id).delete()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Kept oldest "{title}" posting (created {oldest_job.created_at}), '
                    f'removed {dup["count"] - 1} duplicates'
                )
            )
        
        if not duplicates:
            self.stdout.write(self.style.SUCCESS('No duplicate jobs found')) 