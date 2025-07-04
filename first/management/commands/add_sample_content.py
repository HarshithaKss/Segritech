import json
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from first.models import BlogPost, Testimonial


class Command(BaseCommand):
    help = 'Add sample blog posts and testimonials for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample blog posts and testimonials...'))
        
        # Create sample blog posts
        blog_posts_data = [
            {
                'title': 'The Future of AI in Crop Grading and Agricultural Automation',
                'category': 'ai_tech',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Exploring how artificial intelligence is revolutionizing crop quality assessment and transforming agricultural practices across developing nations.',
                'content': '''
                Artificial Intelligence is transforming agriculture at an unprecedented pace. At SegriTech, we're at the forefront of this revolution, developing cutting-edge AI solutions that make crop grading more accurate, efficient, and accessible to farmers worldwide.

                Our AI-powered grading systems use computer vision and machine learning algorithms to assess crop quality with precision that surpasses traditional manual methods. This technology not only reduces human error but also provides consistent, objective quality assessments that help farmers achieve better market prices.

                The impact extends beyond individual farms. By standardizing quality assessment, our AI technology is helping create more transparent and efficient agricultural markets, particularly benefiting smallholder farmers in developing regions who previously lacked access to advanced grading tools.
                ''',
                'comments_count': 12,
                'views_count': 245,
            },
            {
                'title': 'Reducing Post-Harvest Losses: Technology Solutions for Smallholder Farmers',
                'category': 'sustainability',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Innovative approaches to minimize crop waste and maximize farmer profits through smart technology solutions designed for resource-constrained environments.',
                'content': '''
                Post-harvest losses remain one of the biggest challenges facing agriculture globally, with an estimated 40% of crops lost between harvest and market in many developing regions. At SegriTech, we're addressing this challenge through innovative technology solutions specifically designed for smallholder farmers.

                Our grading and sorting machines help farmers identify and separate quality produce, extending shelf life and reducing waste. By catching quality issues early, farmers can make informed decisions about storage, processing, and marketing that significantly reduce losses.

                The economic impact is substantial. Farmers using our technology report average loss reductions of 35-40%, translating directly to increased income and food security for their communities.
                ''',
                'comments_count': 8,
                'views_count': 189,
            },
            {
                'title': 'Empowering Farmers: How Quality Grading Opens Global Market Access',
                'category': 'market_access',
                'author_name': 'Dr. Hetendra Singh',
                'author_title': 'CEO & Founder, SegriTech',
                'excerpt': 'Discover how precision grading technology enables smallholder farmers to compete in international markets and command premium prices for quality produce.',
                'content': '''
                Access to global markets has traditionally been limited for smallholder farmers due to inconsistent quality standards and lack of proper grading infrastructure. SegriTech's precision grading technology is changing this dynamic by providing farmers with the tools they need to meet international quality standards.

                Our machines can sort produce according to various international grading standards, ensuring that farmers can supply consistent quality to export markets. This capability opens up new revenue streams and helps farmers achieve premium prices for their best produce.

                Success stories from our partners demonstrate the transformative power of this technology. Farmers who previously sold only to local markets are now exporting to international buyers, often doubling or tripling their income in the process.
                ''',
                'comments_count': 15,
                'views_count': 320,
            }
        ]

        created_blogs = 0
        updated_blogs = 0

        for blog_data in blog_posts_data:
            slug = slugify(blog_data['title'])
            blog_post, created = BlogPost.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': blog_data['title'],
                    'category': blog_data['category'],
                    'author_name': blog_data['author_name'],
                    'author_title': blog_data['author_title'],
                    'excerpt': blog_data['excerpt'],
                    'content': blog_data['content'],
                    'is_published': True,
                    'published_at': timezone.now() - timedelta(days=created_blogs * 5),
                    'comments_count': blog_data['comments_count'],
                    'views_count': blog_data['views_count'],
                }
            )
            
            if created:
                created_blogs += 1
                self.stdout.write(f'Created blog post: {blog_post.title}')
            else:
                # Update existing blog post
                blog_post.title = blog_data['title']
                blog_post.category = blog_data['category']
                blog_post.author_name = blog_data['author_name']
                blog_post.author_title = blog_data['author_title']
                blog_post.excerpt = blog_data['excerpt']
                blog_post.content = blog_data['content']
                blog_post.is_published = True
                blog_post.comments_count = blog_data['comments_count']
                blog_post.views_count = blog_data['views_count']
                if not blog_post.published_at:
                    blog_post.published_at = timezone.now() - timedelta(days=updated_blogs * 5)
                blog_post.save()
                updated_blogs += 1
                self.stdout.write(f'Updated blog post: {blog_post.title}')

        # Create sample testimonials
        testimonials_data = [
            {
                'name': 'Rajesh Kumar',
                'role': 'farmer',
                'company_or_location': 'Small-Scale Farmer',
                'country': 'India',
                'quote': "SegriTech's AI-powered grading solution revolutionized our farming operations. We've reduced post-harvest losses by 40% and increased market revenue significantly. The technology is incredibly user-friendly and perfect for small-scale farmers like us in developing regions.",
                'impact_metric': '40% Loss Reduction',
                'impact_icon': 'fas fa-chart-line',
                'display_order': 1,
                'rating': 4.8
            },
            {
                'name': 'Maria Santos',
                'role': 'trader',
                'company_or_location': 'Agricultural Trading Company',
                'country': 'Brazil',
                'quote': "As an agricultural trader, precise grading is crucial for our business success. SegriTech's AI-powered solution has improved our operational efficiency by 60% and helped us command premium prices in competitive markets. Essential for modern agribusiness.",
                'impact_metric': '60% Efficiency Boost',
                'impact_icon': 'fas fa-rocket',
                'display_order': 2,
                'rating': 5.0
            },
            {
                'name': 'David Ochieng',
                'role': 'cooperative_manager',
                'company_or_location': 'Farmers Cooperative',
                'country': 'Kenya',
                'quote': "SegriTech's automation technology has completely transformed our cooperative's processing capabilities. We can now grade larger volumes with consistent quality standards, opening new market opportunities for our 500+ member farmers.",
                'impact_metric': '500+ Farmers',
                'impact_icon': 'fas fa-users',
                'display_order': 3,
                'rating': 4.7
            },
            {
                'name': 'Dr. Sarah Ahmed',
                'role': 'extension_officer',
                'company_or_location': 'Agricultural Extension Service',
                'country': 'Nigeria',
                'quote': "Working with SegriTech has been transformational for our agricultural extension program. Their technology helps farmers achieve superior crop quality and better market access, directly improving rural livelihoods across our region.",
                'impact_metric': 'Rural Impact',
                'impact_icon': 'fas fa-globe-africa',
                'display_order': 4,
                'rating': 4.9
            },
            {
                'name': 'James Mwangi',
                'role': 'ngo_director',
                'company_or_location': 'Rural Development NGO',
                'country': 'Tanzania',
                'quote': "SegriTech's solutions are exactly what developing countries need - affordable, accessible, and highly effective. Their crop grading technology has helped reduce waste and significantly improve farmer incomes across multiple communities we support.",
                'impact_metric': 'Community Impact',
                'impact_icon': 'fas fa-heart',
                'display_order': 5,
                'rating': 4.8
            },
        ]

        created_testimonials = 0
        updated_testimonials = 0

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                defaults=testimonial_data
            )
            
            if created:
                created_testimonials += 1
                self.stdout.write(f'Created testimonial: {testimonial.name}')
            else:
                # Update existing testimonial
                for key, value in testimonial_data.items():
                    setattr(testimonial, key, value)
                testimonial.save()
                updated_testimonials += 1
                self.stdout.write(f'Updated testimonial: {testimonial.name}')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSample content creation completed!'
                f'\nBlog Posts: {created_blogs} created, {updated_blogs} updated'
                f'\nTestimonials: {created_testimonials} created, {updated_testimonials} updated'
            )
        ) 