"""
This management command creates an example blog post demonstrating
all the dynamic features of the enhanced blog system.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from first.models import BlogPost
import json

class Command(BaseCommand):
    help = 'Create an example dynamic blog post showcasing all features'

    def handle(self, *args, **options):
        self.stdout.write('Creating dynamic blog post example...')

        # Example gallery images
        gallery_images = [
            {
                "url": "/static/images/blog/List_of_countries.png",
                "caption": "Global export destinations for Indian agriculture",
                "alt": "World map showing countries importing from India"
            },
            {
                "url": "/static/web/bar_graph.png", 
                "caption": "Top importing countries - Market analysis",
                "alt": "Bar chart showing top 10 importing countries"
            }
        ]

        # Example content sections
        content_sections = [
            {
                "type": "text",
                "content": "<h3 style='color: #4CAF50; margin-bottom: 20px;'>🚀 Technology Impact</h3><p>SegriTech's AI-powered sorting technology has revolutionized agricultural processing across India, delivering measurable results for farmers and exporters alike.</p>",
                "style": "background: #f8f9fa; padding: 25px; border-radius: 12px; border-left: 4px solid #4CAF50;",
                "order": 1
            },
            {
                "type": "image",
                "content": "/static/images/blog/Ground.png",
                "style": "width: 100%; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.15); margin: 30px 0;",
                "order": 2
            },
            {
                "type": "quote",
                "content": "SegriTech has processed over 10 million fruits and vegetables, reducing post-harvest losses by 40% and improving export quality standards",
                "style": "font-size: 22px; color: #4CAF50; text-align: center; font-weight: 600; line-height: 1.4; padding: 30px;",
                "order": 3
            },
            {
                "type": "text",
                "content": "<div class='statistics-grid' style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 40px 0;'><div class='stat-card' style='background: white; border: 2px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'><div class='stat-number' style='font-size: 2.5rem; font-weight: bold; color: #4CAF50;'>40%</div><div class='stat-label' style='color: #718096; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;'>Loss Reduction</div></div><div class='stat-card' style='background: white; border: 2px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'><div class='stat-number' style='font-size: 2.5rem; font-weight: bold; color: #4CAF50;'>10M+</div><div class='stat-label' style='color: #718096; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;'>Fruits Processed</div></div><div class='stat-card' style='background: white; border: 2px solid #e2e8f0; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'><div class='stat-number' style='font-size: 2.5rem; font-weight: bold; color: #4CAF50;'>95%</div><div class='stat-label' style='color: #718096; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;'>Accuracy Rate</div></div></div>",
                "order": 4
            }
        ]

        # Custom CSS for enhanced styling
        custom_css = """
<style>
/* Enhanced styling for the dynamic blog post */
.custom-highlight {
    background: linear-gradient(135deg, #4CAF50, #66BB6A);
    color: white;
    padding: 25px;
    border-radius: 12px;
    margin: 30px 0;
    box-shadow: 0 8px 25px rgba(76, 175, 80, 0.3);
}

.technology-showcase {
    background: #f8f9fa;
    border: 2px solid #e2e8f0;
    border-radius: 15px;
    padding: 30px;
    margin: 40px 0;
    position: relative;
    overflow: hidden;
}

.technology-showcase::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #4CAF50, #66BB6A, #4CAF50);
}

.impact-metrics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
    margin: 40px 0;
}

.metric-card {
    background: white;
    border: 3px solid #e8f5e8;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(76, 175, 80, 0.2);
    border-color: #4CAF50;
}

@media (max-width: 768px) {
    .statistics-grid {
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    .stat-number {
        font-size: 2rem !important;
    }
}
</style>
"""

        # Custom JavaScript for interactivity
        custom_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 SegriTech Dynamic Blog Post Loaded');
    
    // Animate statistics numbers
    function animateNumbers() {
        const numberElements = document.querySelectorAll('.stat-number');
        numberElements.forEach(el => {
            const finalText = el.textContent;
            const finalNumber = parseInt(finalText.replace(/[^0-9]/g, ''));
            
            if (finalNumber > 0) {
                let currentNumber = 0;
                const increment = finalNumber / 50;
                
                const timer = setInterval(() => {
                    currentNumber += increment;
                    if (currentNumber >= finalNumber) {
                        el.textContent = finalText;
                        clearInterval(timer);
                    } else {
                        const displayNumber = Math.floor(currentNumber);
                        if (finalText.includes('%')) {
                            el.textContent = displayNumber + '%';
                        } else if (finalText.includes('M+')) {
                            el.textContent = Math.floor(displayNumber/1000000) + 'M+';
                        } else {
                            el.textContent = displayNumber;
                        }
                    }
                }, 30);
            }
        });
    }
    
    // Trigger animation when statistics come into view
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateNumbers();
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe statistics grid
    const statsGrid = document.querySelector('.statistics-grid');
    if (statsGrid) {
        observer.observe(statsGrid);
    }
    
    // Add smooth hover effects to metric cards
    const metricCards = document.querySelectorAll('.metric-card');
    metricCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.background = 'linear-gradient(135deg, #f0fff4, #e8f5e8)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.background = 'white';
        });
    });
    
    // Smooth scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    console.log('✅ All interactive features loaded successfully!');
});
</script>
"""

        # Main content with HTML
        content = """
<h1 style="color: #2d3748; margin-bottom: 25px;">Transforming Agriculture with AI-Powered Technology</h1>

<p style="font-size: 1.1rem; line-height: 1.6; color: #4a5568; margin-bottom: 30px;">
India's agricultural sector is experiencing a technological revolution. SegriTech is at the forefront of this transformation, 
delivering AI-powered sorting and grading solutions that address critical challenges in post-harvest processing.
</p>

<div class="technology-showcase">
    <h3 style="color: #4CAF50; margin-bottom: 20px; font-size: 1.5rem;">🔬 Advanced Technology Stack</h3>
    <p style="margin-bottom: 20px;">Our proprietary AI algorithms combine computer vision, machine learning, and real-time data processing to deliver unprecedented accuracy in agricultural sorting.</p>
    
    <ul style="list-style: none; padding: 0;">
        <li style="margin: 10px 0; padding: 10px 0; border-bottom: 1px solid #e2e8f0;">
            <strong>🤖 Computer Vision:</strong> Advanced image recognition for size, color, and defect detection
        </li>
        <li style="margin: 10px 0; padding: 10px 0; border-bottom: 1px solid #e2e8f0;">
            <strong>📊 Machine Learning:</strong> Continuous improvement through data-driven optimization
        </li>
        <li style="margin: 10px 0; padding: 10px 0; border-bottom: 1px solid #e2e8f0;">
            <strong>⚡ Real-time Processing:</strong> High-speed sorting up to 2 tons per hour
        </li>
        <li style="margin: 10px 0; padding: 10px 0;">
            <strong>📱 IoT Integration:</strong> Remote monitoring and predictive maintenance
        </li>
    </ul>
</div>

<h2 style="color: #2d3748; margin: 40px 0 25px 0;">Market Impact & Results</h2>

<p style="margin-bottom: 25px;">
Our technology has been deployed across India, from small-scale farmers to large export facilities. 
The results speak for themselves - significant reduction in post-harvest losses, improved quality standards, 
and enhanced market access for Indian agricultural products.
</p>

<div class="custom-highlight">
    <h4 style="margin: 0 0 15px 0; font-size: 1.3rem;">🌟 Success Story</h4>
    <p style="margin: 0; font-size: 1.1rem; line-height: 1.5;">
        "Working with SegriTech has transformed our operations. We've reduced waste by 40% and increased our export quality ratings. 
        The technology pays for itself within months." - Rajesh Kumar, Agricultural Cooperative Manager
    </p>
</div>

<h2 style="color: #2d3748; margin: 40px 0 25px 0;">Future of Agricultural Technology</h2>

<p style="margin-bottom: 25px;">
As we look toward the future, SegriTech continues to innovate. Our roadmap includes advanced robotics integration, 
blockchain-based traceability systems, and AI-powered predictive analytics for crop optimization.
</p>

<div style="background: linear-gradient(135deg, #4CAF50, #66BB6A); color: white; padding: 30px; border-radius: 12px; text-align: center; margin: 40px 0;">
    <h3 style="margin: 0 0 15px 0;">Ready to Transform Your Agricultural Operations?</h3>
    <p style="margin: 0 0 20px 0; opacity: 0.9;">Discover how SegriTech's solutions can reduce your post-harvest losses by up to 40%.</p>
    <a href="/contact/" style="background: white; color: #4CAF50; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;">Get Started Today →</a>
</div>
"""

        # Create the blog post
        blog_post = BlogPost.objects.create(
            title='Dynamic Blog Post Example: AI-Powered Agricultural Technology',
            slug='dynamic-blog-example-ai-agricultural-technology',
            category='technology',
            author_name='Dr. Hetendra Singh',
            author_title='CEO & Founder, SegriTech',
            excerpt='Explore how SegriTech is revolutionizing agriculture through AI-powered sorting technology, reducing post-harvest losses by 40% and transforming the industry.',
            content=content,
            gallery_images=json.dumps(gallery_images),
            content_sections=json.dumps(content_sections),
            custom_css=custom_css,
            custom_js=custom_js,
            video_url='',  # You can add a YouTube URL here if needed
            estimated_read_time=8,
            is_published=True,
            is_featured=False,  # Set to True if you want it on homepage
            published_at=timezone.now(),
            tags='AI, agriculture, technology, sorting, innovation, segritech, farming, automation, post-harvest',
            meta_title='AI-Powered Agricultural Technology | SegriTech Innovation',
            meta_description='Discover how SegriTech\'s AI-powered sorting technology is transforming agriculture, reducing losses by 40% and improving quality standards across India.'
        )

        self.stdout.write(
            self.style.SUCCESS(f'✅ Created dynamic blog post: "{blog_post.title}"')
        )
        self.stdout.write(
            self.style.SUCCESS(f'🔗 Access it at: /blog/{blog_post.slug}/')
        )
        self.stdout.write(
            self.style.WARNING('💡 To feature this post on homepage, set "is_featured=True" in admin')
        ) 