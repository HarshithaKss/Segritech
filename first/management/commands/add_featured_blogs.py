from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.files import File
from django.conf import settings
from first.models import BlogPost
from django.utils.text import slugify
import os
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Add featured blog posts'

    def handle(self, *args, **options):
        try:
            # Blog data
            blogs_data = [
                {
                    'title': "Revolutionizing Quality Control",
                    'slug': "revolutionizing-quality-control",
                    'category': 'technology',
                    'author_name': "Dr. Hetendra Singh",
                    'author_title': "CEO & Founder, SegriTech",
                    'excerpt': "Discover how artificial intelligence is transforming fruit quality assessment, reducing waste, and improving supply chain efficiency in the agricultural sector.",
                    'content': """Artificial Intelligence is revolutionizing how we assess and grade fruit quality in the agricultural sector. Through advanced computer vision and machine learning algorithms, we can now achieve unprecedented accuracy in detecting defects, measuring size, and evaluating ripeness.

Key Benefits:
• Consistent and objective quality assessment
• Reduced waste through early defect detection
• Improved supply chain efficiency
• Real-time data analytics for better decision making

Our AI-powered grading systems are helping farmers and processors:
1. Increase throughput while maintaining accuracy
2. Reduce labor costs and human error
3. Meet strict export quality standards
4. Optimize sorting and packaging operations

The future of quality control is here, and it's powered by artificial intelligence.""",
                    'image_path': 'static/images/blog/Export_fruit.png',
                    'tags': 'AI, Quality Control, Agriculture, Technology, Innovation'
                },
                {
                    'title': "Sustainable Agriculture Through Smart Technology",
                    'slug': "sustainable-agriculture-through-smart-technology",
                    'category': 'sustainability',
                    'author_name': "Dr. Hetendra Singh",
                    'author_title': "CEO & Founder, SegriTech",
                    'excerpt': "Explore how smart agricultural technologies are helping farmers adopt more sustainable practices while maintaining profitability.",
                    'content': """Smart agricultural technologies are transforming traditional farming practices into sustainable, efficient operations. By leveraging IoT sensors, data analytics, and automated systems, farmers can optimize resource usage while improving yields.

Key Technologies:
• Precision irrigation systems
• Smart nutrient management
• Automated grading and sorting
• Integrated pest management

Benefits for Farmers:
1. Reduced water consumption
2. Optimized fertilizer usage
3. Minimized crop losses
4. Improved product quality

The integration of smart technology in agriculture is not just about efficiency—it's about creating a sustainable future for farming.""",
                    'image_path': 'static/images/blog/Ground.png',
                    'tags': 'Sustainability, Smart Agriculture, IoT, Technology, Farming'
                },
                {
                    'title': "From Farm to Table: Improving Market Access for Small Farmers",
                    'slug': "from-farm-to-table-improving-market-access",
                    'category': 'case_study',
                    'author_name': "Dr. Hetendra Singh",
                    'author_title': "CEO & Founder, SegriTech",
                    'excerpt': "Learn how modern post-harvest technologies are helping small farmers reach premium markets and improve their income.",
                    'content': """Small farmers often face significant challenges in accessing premium markets due to quality control and post-harvest handling requirements. Modern technology is bridging this gap by making professional-grade sorting and grading accessible to small-scale operations.

Key Challenges Addressed:
• Quality consistency
• Market access barriers
• Post-harvest losses
• Price realization

Solutions Implemented:
1. Portable grading machines
2. Mobile quality assessment tools
3. Cold chain solutions
4. Market linkage platforms

By adopting these technologies, small farmers can compete effectively in premium markets and secure better returns for their produce.""",
                    'image_path': 'static/images/blog/List_of_countries.png',
                    'tags': 'Small Farmers, Market Access, Post-harvest Technology, Case Study'
                }
            ]

            # Create blogs
            for blog_data in blogs_data:
                # Check if blog already exists
                if not BlogPost.objects.filter(title=blog_data['title']).exists():
                    # Create the blog post
                    blog = BlogPost(
                        title=blog_data['title'],
                        slug=blog_data['slug'],
                        category=blog_data['category'],
                        author_name=blog_data['author_name'],
                        author_title=blog_data['author_title'],
                        excerpt=blog_data['excerpt'],
                        content=blog_data['content'],
                        is_featured=True,
                        is_published=True,
                        published_at=timezone.now() - timedelta(days=1),
                        created_at=timezone.now(),
                        updated_at=timezone.now(),
                        tags=blog_data['tags'],
                        estimated_read_time=5
                    )
                    blog.save()

                    # Add the image
                    image_path = os.path.join(settings.BASE_DIR, blog_data['image_path'])
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as img_file:
                            blog.featured_image.save(
                                os.path.basename(image_path),
                                File(img_file),
                                save=True
                            )
                    
                    self.stdout.write(self.style.SUCCESS(f'Successfully created blog: {blog_data["title"]}'))
                else:
                    # Update existing blog
                    blog = BlogPost.objects.get(title=blog_data['title'])
                    blog.slug = blog_data['slug']
                    blog.category = blog_data['category']
                    blog.author_name = blog_data['author_name']
                    blog.author_title = blog_data['author_title']
                    blog.excerpt = blog_data['excerpt']
                    blog.content = blog_data['content']
                    blog.is_featured = True
                    blog.is_published = True
                    blog.tags = blog_data['tags']
                    blog.updated_at = timezone.now()
                    
                    # Update the image
                    image_path = os.path.join(settings.BASE_DIR, blog_data['image_path'])
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as img_file:
                            blog.featured_image.save(
                                os.path.basename(image_path),
                                File(img_file),
                                save=True
                            )
                    
                    blog.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated blog: {blog_data["title"]}'))

            self.stdout.write(self.style.SUCCESS('Successfully processed all blog posts'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}')) 