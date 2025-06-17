from django.core.management.base import BaseCommand
from first.models import MediaCoverageArticle


class Command(BaseCommand):
    help = 'View all media coverage articles in the database'

    def handle(self, *args, **options):
        self.stdout.write('📊 MEDIA COVERAGE ARTICLES DATABASE')
        self.stdout.write('=' * 60)
        
        articles = MediaCoverageArticle.objects.all().order_by('display_order')
        
        if not articles.exists():
            self.stdout.write(self.style.WARNING('❌ No articles found in database'))
            self.stdout.write('Run: python manage.py populate_media_articles')
            return
        
        for i, article in enumerate(articles, 1):
            status = "🟢" if article.is_active else "🔴"
            featured = "⭐" if article.is_featured else "  "
            
            self.stdout.write(f'\n{status}{featured} {i}. {article.title}')
            self.stdout.write(f'     📰 Publication: {article.publication}')
            self.stdout.write(f'     📂 Category: {article.get_category_display()}')
            self.stdout.write(f'     📅 Date: {article.publication_date}')
            self.stdout.write(f'     🔗 URL: {article.article_url}')
            self.stdout.write(f'     📊 Order: {article.display_order} | Clicks: {article.clicks_count}')
            self.stdout.write(f'     🎨 Icon: {article.icon}')
        
        # Summary
        total = articles.count()
        active = articles.filter(is_active=True).count()
        featured = articles.filter(is_featured=True).count()
        
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(f'📈 SUMMARY:')
        self.stdout.write(f'   Total Articles: {total}')
        self.stdout.write(f'   🟢 Active: {active}')
        self.stdout.write(f'   🔴 Inactive: {total - active}')
        self.stdout.write(f'   ⭐ Featured: {featured}')
        self.stdout.write('=' * 60)
        self.stdout.write('💡 To manage articles: http://localhost:8000/admin/') 