from django.core.management.base import BaseCommand
from django.utils import timezone
from first.models import BlogPost
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Add sample blog posts for testing'

    def handle(self, *args, **options):
        blog_posts = [
            {
                'title': 'AI-Powered Fruit Grading: Revolutionizing Quality Control',
                'slug': 'ai-powered-fruit-grading-revolutionizing-quality-control',
                'category': 'ai_tech',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Discover how artificial intelligence is transforming fruit quality assessment, reducing waste, and improving supply chain efficiency in the agricultural sector.',
                'content': '''
<h2>The Future of Agricultural Quality Control</h2>
<p>In today's rapidly evolving agricultural landscape, the integration of artificial intelligence has become a game-changer for fruit grading and quality control. Our AI-powered grading systems are setting new standards for accuracy and efficiency.</p>

<h3>Key Benefits of AI Grading:</h3>
<ul>
<li>99.2% accuracy in quality classification</li>
<li>60% reduction in post-harvest losses</li>
<li>50% faster processing compared to manual methods</li>
<li>Consistent quality standards across different operators</li>
</ul>

<h3>Technology Behind the Innovation</h3>
<p>Our grading systems utilize advanced computer vision algorithms combined with machine learning models trained on millions of fruit images. This enables precise classification based on size, color, defects, and ripeness levels.</p>

<p>The impact on farmers has been remarkable, with many reporting significant improvements in their market prices due to better quality sorting and reduced rejection rates.</p>
                ''',
                'is_published': True,
                'is_featured': True,
                'published_at': timezone.now() - timedelta(days=2),
            },
            {
                'title': 'Sustainable Agriculture Through Smart Technology',
                'slug': 'sustainable-agriculture-through-smart-technology',
                'category': 'sustainability',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Explore how smart agricultural technologies are helping farmers adopt more sustainable practices while maintaining profitability.',
                'content': '''
<h2>Building a Sustainable Future</h2>
<p>Sustainability in agriculture is no longer just an option—it's a necessity. Smart technologies are enabling farmers to produce more with less environmental impact.</p>

<h3>Our Approach to Sustainable Farming:</h3>
<ul>
<li>Precision sorting to reduce food waste</li>
<li>Energy-efficient processing systems</li>
<li>Data-driven farming insights</li>
<li>Reduced chemical usage through better quality assessment</li>
</ul>

<p>By implementing our technologies, farmers have reported up to 40% reduction in post-harvest losses, directly contributing to more sustainable food systems.</p>
                ''',
                'is_published': True,
                'published_at': timezone.now() - timedelta(days=5),
            },
            {
                'title': 'From Farm to Table: Improving Market Access for Small Farmers',
                'slug': 'from-farm-to-table-improving-market-access',
                'category': 'market_access',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Learn how technology is bridging the gap between small-scale farmers and premium markets, creating new opportunities for rural communities.',
                'content': '''
<h2>Empowering Small-Scale Farmers</h2>
<p>Small farmers often struggle to access premium markets due to inconsistent quality and lack of proper grading facilities. Our portable grading solutions are changing this narrative.</p>

<h3>Impact on Farmer Communities:</h3>
<ul>
<li>30% increase in average selling prices</li>
<li>Direct access to premium retail chains</li>
<li>Reduced dependency on middlemen</li>
<li>Better negotiating power in markets</li>
</ul>

<p>Through our technology partnerships, we've helped over 500 farmers across India gain access to better markets and improve their livelihoods.</p>
                ''',
                'is_published': True,
                'published_at': timezone.now() - timedelta(days=8),
            },
        ]

        created_count = 0
        for blog_data in blog_posts:
            blog_post, created = BlogPost.objects.get_or_create(
                slug=blog_data['slug'],
                defaults=blog_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created blog post: {blog_post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Blog post already exists: {blog_post.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSummary: {created_count} new blog posts created')
        ) 