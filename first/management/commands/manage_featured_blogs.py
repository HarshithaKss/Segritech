from django.core.management.base import BaseCommand
from first.models import BlogPost

class Command(BaseCommand):
    help = 'Manage featured blog posts that appear on the homepage'

    def add_arguments(self, parser):
        parser.add_argument(
            '--list-featured',
            action='store_true',
            help='List all currently featured blog posts',
        )
        parser.add_argument(
            '--set-featured',
            type=str,
            help='Set blog post as featured by slug',
        )
        parser.add_argument(
            '--unset-featured',
            type=str,
            help='Remove blog post from featured by slug',
        )
        parser.add_argument(
            '--clear-all-featured',
            action='store_true',
            help='Remove all blog posts from featured (none will show on homepage)',
        )
        parser.add_argument(
            '--featured-count',
            action='store_true',
            help='Show count of featured blog posts',
        )

    def handle(self, *args, **options):
        if options['list_featured']:
            self.list_featured()
        elif options['set_featured']:
            self.set_featured(options['set_featured'])
        elif options['unset_featured']:
            self.unset_featured(options['unset_featured'])
        elif options['clear_all_featured']:
            self.clear_all_featured()
        elif options['featured_count']:
            self.featured_count()
        else:
            self.stdout.write(self.style.WARNING('Please specify an action. Use --help for options.'))

    def list_featured(self):
        featured_posts = BlogPost.objects.filter(is_published=True, is_featured=True).order_by('-published_at')
        
        if not featured_posts:
            self.stdout.write(self.style.WARNING('No featured blog posts found.'))
            return
            
        self.stdout.write(self.style.SUCCESS(f'\nFeatured Blog Posts ({featured_posts.count()}):'))
        self.stdout.write('-' * 60)
        
        for i, post in enumerate(featured_posts, 1):
            self.stdout.write(f'{i}. {post.title}')
            self.stdout.write(f'   Slug: {post.slug}')
            self.stdout.write(f'   Author: {post.author_name}')
            self.stdout.write(f'   Published: {post.published_at.strftime("%Y-%m-%d") if post.published_at else "Not set"}')
            self.stdout.write(f'   Views: {post.views_count}')
            self.stdout.write('')

    def set_featured(self, slug):
        try:
            post = BlogPost.objects.get(slug=slug, is_published=True)
            if post.is_featured:
                self.stdout.write(self.style.WARNING(f'"{post.title}" is already featured.'))
            else:
                post.is_featured = True
                post.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully set "{post.title}" as featured.'))
        except BlogPost.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Published blog post with slug "{slug}" not found.'))

    def unset_featured(self, slug):
        try:
            post = BlogPost.objects.get(slug=slug, is_published=True, is_featured=True)
            post.is_featured = False
            post.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully removed "{post.title}" from featured.'))
        except BlogPost.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Featured blog post with slug "{slug}" not found.'))

    def clear_all_featured(self):
        featured_count = BlogPost.objects.filter(is_featured=True).count()
        if featured_count == 0:
            self.stdout.write(self.style.WARNING('No featured blog posts to clear.'))
            return
            
        BlogPost.objects.filter(is_featured=True).update(is_featured=False)
        self.stdout.write(self.style.SUCCESS(f'Successfully cleared {featured_count} featured blog posts.'))
        self.stdout.write(self.style.WARNING('Note: No blog posts will appear on the homepage until you set some as featured.'))

    def featured_count(self):
        total_published = BlogPost.objects.filter(is_published=True).count()
        featured_count = BlogPost.objects.filter(is_published=True, is_featured=True).count()
        
        self.stdout.write(f'Total published blog posts: {total_published}')
        self.stdout.write(f'Featured blog posts: {featured_count}')
        
        if featured_count == 0:
            self.stdout.write(self.style.WARNING('⚠️  No featured blog posts - homepage will show empty insights section!'))
        elif featured_count > 3:
            self.stdout.write(self.style.WARNING(f'⚠️  {featured_count} featured posts found - only the 3 most recent will show on homepage.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'✅ Perfect! {featured_count} featured posts will show on homepage.')) 