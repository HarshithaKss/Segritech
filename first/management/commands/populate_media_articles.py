from django.core.management.base import BaseCommand
from first.models import MediaCoverageArticle
from datetime import date


class Command(BaseCommand):
    help = 'Populate media coverage articles with existing data'

    def handle(self, *args, **options):
        # Clear existing articles
        self.stdout.write('🗑️  Clearing existing articles...')
        deleted_count = MediaCoverageArticle.objects.all().count()
        MediaCoverageArticle.objects.all().delete()
        self.stdout.write(f'Deleted {deleted_count} existing articles')
        
        # Create articles from existing data
        articles_data = [
            {
                'title': '$100K Pre-Seed Funding Success',
                'publication': 'LeadsOnTrees',
                'category': 'funding',
                'icon': 'fa-leaf',
                'description': 'SegriTech secures funding to scale AI-powered grading solutions for fruits and vegetables, highlighting plans to improve AI accuracy and reach new markets.',
                'article_url': 'https://leadsontrees.com/segritech-secures-100000-in-pre-seed-funding-to-revolutionize-agriculture-supply-chain-with-ai-grading-solution/',
                'publication_date': date(2024, 1, 15),
                'display_order': 1,
                'is_featured': True,
            },
            {
                'title': 'Deep-Tech Startup Founders',
                'publication': 'The New Indian Express',
                'category': 'founder_spotlight',
                'icon': 'fa-newspaper',
                'description': 'Hetendra Singh featured among Hyderabad\'s prominent deep-tech startup founders, emphasizing SegriTech\'s world\'s first compact, movable smart sorting machine.',
                'article_url': 'https://www.newindianexpress.com/cities/hyderabad/2025/Jan/16/hyderabads-startup-ecosystem-founders-share-challenges-growth-and-aspirations-for-the-citys-future',
                'publication_date': date(2024, 1, 16),
                'display_order': 2,
                'is_featured': True,
            },
            {
                'title': 'CIE-IIITH Demo Day',
                'publication': 'The Hindu BusinessLine',
                'category': 'demo_day',
                'icon': 'fa-chart-line',
                'description': 'SegriTech showcased at CIE-IIITH Demo Day alongside 12 deep-tech startups for its smart sorting machine targeting fresh produce.',
                'article_url': 'https://www.thehindubusinessline.com/news/12-deeptech-start-ups-at-cie-iiith-pitch-products/article67707890.ece',
                'publication_date': date(2024, 2, 10),
                'display_order': 3,
                'is_featured': False,
            },
            {
                'title': 'Avishkar Accelerator Cohort',
                'publication': 'StartUp Hyderabad',
                'category': 'accelerator',
                'icon': 'fa-rocket',
                'description': 'CIE-IITH onboards 9 startups including SegriTech for Avishkar 16 accelerator cohort. SegriTech raised ₹11.35L through this program.',
                'article_url': 'https://startuphyderabad.com/cie-iith-onboards-9-startups-for-its-accelerator-cohorts/',
                'publication_date': date(2024, 3, 5),
                'display_order': 4,
                'is_featured': False,
            },
            {
                'title': 'AI Technology Impact',
                'publication': 'Industry Analysis',
                'category': 'technology_impact',
                'icon': 'fa-industry',
                'description': 'AI-powered grading systems like SegriTech\'s enabling Telangana farmers to get quality reports in 20-25 minutes, transforming supply chains.',
                'article_url': 'https://www.thehindubusinessline.com',
                'publication_date': date(2024, 4, 1),
                'display_order': 5,
                'is_featured': False,
            },
            {
                'title': 'AgriTech Innovation',
                'publication': '18StartUp',
                'category': 'agritech_coverage',
                'icon': 'fa-seedling',
                'description': 'Coverage of AI-powered grading systems and their revolutionary impact on agricultural supply chains and farmer productivity.',
                'article_url': 'https://18startup.com',
                'publication_date': date(2024, 5, 15),
                'display_order': 6,
                'is_featured': False,
            },
        ]
        
        self.stdout.write('📝 Creating articles...')
        created_count = 0
        for i, article_data in enumerate(articles_data, 1):
            try:
                article = MediaCoverageArticle.objects.create(**article_data)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ {i}/6 Created: {article.title}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ {i}/6 Failed: {article_data["title"]} - Error: {str(e)}')
                )
        
        total_articles = MediaCoverageArticle.objects.count()
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS(f'🎉 Successfully created {created_count} media coverage articles!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'📊 Total articles in database: {total_articles}')
        )
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS('🔧 You can now manage these articles in Django Admin:')
        )
        self.stdout.write('   1. Go to: http://localhost:8000/admin/')
        self.stdout.write('   2. Login with your superuser account')
        self.stdout.write('   3. Click "Media Coverage Articles"')
        self.stdout.write('   4. Add, edit, delete, or reorder articles')
        self.stdout.write('')
        self.stdout.write('🌟 Website will automatically load articles from database!') 