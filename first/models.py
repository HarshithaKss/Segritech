from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    INQUIRY_CHOICES = [
        ('general', 'General Inquiry'),
        ('product', 'Product Information'),
        ('support', 'Technical Support'),
        ('partnership', 'Partnership Opportunity'),
        ('demo', 'Request Demo'),
        ('pricing', 'Pricing Information'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_CHOICES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class ProductCategory(models.Model):
    CATEGORY_CHOICES = [
        ('size_graders', 'Size Graders'),
        ('quality_graders', 'Quality Graders'),
        ('weight_graders', 'Weight Graders'),
        ('cleaning_machines', 'Cleaning Machines'),
        ('packing_robots', 'Packing Robots'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/', help_text='Category banner image')
    icon = models.CharField(max_length=50, help_text='FontAwesome icon class', default='fas fa-cogs')
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', 'name']
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    detailed_description = models.TextField()
    
    # Technical Specifications
    specifications = models.TextField(help_text='Technical specifications in JSON or structured format')
    dimensions = models.CharField(max_length=100, blank=True, help_text='L x W x H')
    weight = models.CharField(max_length=50, blank=True)
    power_requirements = models.CharField(max_length=100, blank=True)
    capacity = models.CharField(max_length=100, blank=True, help_text='Processing capacity per hour')
    
    # Media
    main_image = models.ImageField(upload_to='products/', blank=True)
    gallery_images = models.TextField(blank=True, help_text='Comma-separated list of image URLs')
    video_url = models.URLField(blank=True, help_text='YouTube or Vimeo URL')
    brochure = models.FileField(upload_to='brochures/', blank=True)
    
    # Pricing and Availability
    price_range = models.CharField(max_length=100, blank=True, help_text='e.g., ₹50,000 - ₹75,000')
    is_available = models.BooleanField(default=True)
    lead_time = models.CharField(max_length=50, blank=True, help_text='Manufacturing/delivery time')
    
    # Features and Benefits
    key_features = models.TextField(help_text='JSON list of key features')
    applications = models.TextField(help_text='Suitable applications and use cases')
    benefits = models.TextField(help_text='Key benefits and advantages')
    
    # SEO and Meta
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'display_order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ProductInquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=[
        ('pricing', 'Pricing Information'),
        ('demo', 'Request Demo'),
        ('specs', 'Technical Specifications'),
        ('customization', 'Customization Options'),
        ('bulk_order', 'Bulk Order Inquiry'),
        ('partnership', 'Partnership Opportunity'),
    ])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product Inquiry'
        verbose_name_plural = 'Product Inquiries'
    
    def __str__(self):
        return f"{self.name} - {self.product.name}"


class JobPosting(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
        ('remote', 'Remote'),
    ]
    
    EXPERIENCE_LEVEL_CHOICES = [
        ('entry', 'Entry Level'),
        ('junior', 'Junior (1-3 years)'),
        ('mid', 'Mid Level (3-5 years)'),
        ('senior', 'Senior (5+ years)'),
        ('lead', 'Lead/Principal'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('engineering', 'Engineering & Development'),
        ('ai_ml', 'AI & Machine Learning'),
        ('hardware', 'Hardware & Robotics'),
        ('product', 'Product Management'),
        ('sales', 'Sales & Marketing'),
        ('operations', 'Operations'),
        ('finance', 'Finance & Administration'),
        ('hr', 'Human Resources'),
    ]
    
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    location = models.CharField(max_length=100, default='Bangalore, India')
    remote_allowed = models.BooleanField(default=False)
    
    # Job Details
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    nice_to_have = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    
    # Salary and Benefits
    salary_min = models.IntegerField(blank=True, null=True, help_text='Minimum salary in INR per annum')
    salary_max = models.IntegerField(blank=True, null=True, help_text='Maximum salary in INR per annum')
    equity_offered = models.BooleanField(default=False)
    
    # Meta Information
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    applications_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['-is_featured', '-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.get_job_type_display()}"
    
    @property
    def salary_range(self):
        if self.salary_min and self.salary_max:
            return f"₹{self.salary_min:,} - ₹{self.salary_max:,} per annum"
        elif self.salary_min:
            return f"₹{self.salary_min:,}+ per annum"
        return "Competitive"


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Application Submitted'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interview_completed', 'Interview Completed'),
        ('offer_extended', 'Offer Extended'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]
    
    # Job and Applicant Info
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    
    # Personal Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_location = models.CharField(max_length=100)
    willing_to_relocate = models.BooleanField(default=False)
    
    # Professional Information
    current_company = models.CharField(max_length=100, blank=True)
    current_role = models.CharField(max_length=100, blank=True)
    years_experience = models.CharField(max_length=20, choices=[
        ('0', 'Fresh Graduate'),
        ('1', '1 Year'),
        ('2', '2 Years'),
        ('3', '3 Years'),
        ('4', '4 Years'),
        ('5', '5 Years'),
        ('6-10', '6-10 Years'),
        ('10+', '10+ Years'),
    ])
    
    # Application Materials
    resume = models.FileField(upload_to='resumes/', help_text='Upload your resume (PDF format preferred)')
    cover_letter = models.TextField(help_text='Tell us why you want to join SegriTech')
    portfolio_url = models.URLField(blank=True, help_text='Link to your portfolio/GitHub/LinkedIn')
    
    # Additional Information
    expected_salary = models.IntegerField(blank=True, null=True, help_text='Expected salary in INR per annum')
    earliest_start_date = models.DateField(help_text='When can you start?')
    visa_sponsorship_required = models.BooleanField(default=False)
    
    # References
    reference1_name = models.CharField(max_length=100, blank=True)
    reference1_email = models.EmailField(blank=True)
    reference1_phone = models.CharField(max_length=20, blank=True)
    reference1_relation = models.CharField(max_length=100, blank=True)
    
    # Application Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    notes = models.TextField(blank=True, help_text='Internal notes for HR team')
    
    # Timestamps
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-applied_at']
        unique_together = ['job_posting', 'email']  # Prevent duplicate applications
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_posting.title}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('automation', 'Automation'),
        ('research', 'Research'),
        ('case_study', 'Case Study'),
        ('industry_news', 'Industry News'),
        ('market-analysis', 'Market Analysis'),
        ('technology', 'Technology'),
        ('sustainability', 'Sustainability'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100, help_text='e.g., Research Scientist, Product Manager')
    author_image = models.ImageField(upload_to='blog_authors/', blank=True)
    
    # Content
    excerpt = models.CharField(max_length=300, help_text='Short description shown on cards')
    content = models.TextField(help_text='Full blog post content (supports HTML)')
    featured_image = models.ImageField(upload_to='blog_images/', help_text='Main image shown in cards and at top of article')
    
    # Additional Media Support
    gallery_images = models.TextField(blank=True, help_text='JSON array of additional images for the blog post - format: [{"url": "/static/images/blog/image1.jpg", "caption": "Image caption", "alt": "Alt text"}]')
    video_url = models.URLField(blank=True, help_text='YouTube/Vimeo URL for embedded video')
    
    # Custom Styling Support
    custom_css = models.TextField(blank=True, help_text='Custom CSS styles for this blog post only. Use <style> tags.')
    custom_js = models.TextField(blank=True, help_text='Custom JavaScript for interactive elements. Use <script> tags.')
    
    # Content Sections Support
    content_sections = models.TextField(blank=True, help_text='JSON array for structured content sections - format: [{"type": "text|image|video|chart|quote", "content": "...", "style": "...", "order": 1}]')
    
    # External Links
    external_url = models.URLField(blank=True, help_text='External URL (e.g., LinkedIn article link) - if provided, clicking will redirect to this URL')
    
    # Meta Information
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text='Comma-separated tags')
    
    # Reading Metrics
    estimated_read_time = models.IntegerField(default=5, help_text='Estimated reading time in minutes')
    
    # Status
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
    
    def get_category_display_with_icon(self):
        category_icons = {
            'automation': 'fas fa-cogs',
            'research': 'fas fa-microscope',
            'case_study': 'fas fa-chart-line',
            'industry_news': 'fas fa-newspaper',
            'market-analysis': 'fas fa-chart-bar',
            'technology': 'fas fa-laptop',
            'sustainability': 'fas fa-leaf',
        }
        return {
            'name': self.get_category_display(),
            'icon': category_icons.get(self.category, 'fas fa-newspaper')
        }


class Testimonial(models.Model):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('trader', 'Agricultural Trader'),
        ('cooperative_manager', 'Cooperative Manager'),
        ('extension_officer', 'Extension Officer'),
        ('ngo_director', 'NGO Director'),
        ('export_manager', 'Export Manager'),
        ('researcher', 'Research Scientist'),
        ('entrepreneur', 'Agricultural Entrepreneur'),
        ('consultant', 'Agricultural Consultant'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    company_or_location = models.CharField(max_length=150, help_text='Company name or location')
    country = models.CharField(max_length=50)
    
    # Testimonial Content
    quote = models.TextField(help_text='The testimonial quote')
    impact_metric = models.CharField(max_length=100, help_text='e.g., 40% Loss Reduction, 500+ Farmers')
    impact_icon = models.CharField(max_length=50, default='fas fa-chart-line', help_text='FontAwesome icon class')
    
    # Media
    photo = models.ImageField(upload_to='testimonials/')
    video_url = models.URLField(blank=True, help_text='Optional video testimonial URL')
    
    # Status and Display
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"
    
    def get_role_icon(self):
        role_icons = {
            'farmer': 'fas fa-tractor',
            'trader': 'fas fa-handshake',
            'cooperative_manager': 'fas fa-users-cog',
            'extension_officer': 'fas fa-leaf',
            'ngo_director': 'fas fa-hands-helping',
            'export_manager': 'fas fa-shipping-fast',
            'researcher': 'fas fa-flask',
            'entrepreneur': 'fas fa-seedling',
            'consultant': 'fas fa-user-tie',
        }
        return role_icons.get(self.role, 'fas fa-user')


class MediaCoverageArticle(models.Model):
    CATEGORY_CHOICES = [
        ('funding', 'Funding News'),
        ('founder_spotlight', 'Founder Spotlight'),
        ('demo_day', 'Demo Day'),
        ('accelerator', 'Accelerator'),
        ('awards', 'Awards & Recognition'),
        ('technology_impact', 'Technology Impact'),
        ('agritech_coverage', 'AgriTech Coverage'),
        ('industry_analysis', 'Industry Analysis'),
        ('partnership', 'Partnership'),
        ('product_launch', 'Product Launch'),
        ('research', 'Research & Development'),
        ('sustainability', 'Sustainability'),
    ]
    
    ICON_CHOICES = [
        ('fa-leaf', 'Leaf (Environment/Agriculture)'),
        ('fa-newspaper', 'Newspaper (General News)'),
        ('fa-chart-line', 'Chart Line (Growth/Analytics)'),
        ('fa-rocket', 'Rocket (Startups/Innovation)'),
        ('fa-industry', 'Industry (Technology)'),
        ('fa-seedling', 'Seedling (AgriTech)'),
        ('fa-globe', 'Globe (Global/International)'),
        ('fa-lightbulb', 'Lightbulb (Innovation)'),
        ('fa-trophy', 'Trophy (Awards)'),
        ('fa-medal', 'Medal (Achievement)'),
        ('fa-star', 'Star (Featured/Important)'),
        ('fa-award', 'Award (Recognition)'),
        ('fa-briefcase', 'Briefcase (Business)'),
        ('fa-handshake', 'Handshake (Partnership)'),
        ('fa-users', 'Users (Community)'),
        ('fa-cogs', 'Cogs (Technology)'),
        ('fa-bullhorn', 'Bullhorn (Announcement)'),
        ('fa-camera', 'Camera (Media)'),
        ('fa-microphone', 'Microphone (Interview)'),
        ('fa-tv', 'TV (Broadcast)'),
        ('fa-wifi', 'WiFi (Digital/Tech)'),
        ('fa-mobile', 'Mobile (Apps/Mobile)'),
        ('fa-laptop', 'Laptop (Software)'),
        ('fa-desktop', 'Desktop (Systems)'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200, help_text='Article headline/title')
    publication = models.CharField(max_length=100, help_text='Name of the publication')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='agritech_coverage')
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='fa-newspaper', 
                           help_text='FontAwesome icon to display with the article')
    
    # Content
    description = models.TextField(help_text='Brief description of the article (max 300 characters recommended)')
    article_url = models.URLField(help_text='Direct link to the article')
    
    # Media
    featured_image = models.ImageField(upload_to='media_coverage/', blank=True, 
                                     help_text='Optional image for the article card')
    
    # Metadata
    publication_date = models.DateField(help_text='Date when the article was published')
    is_featured = models.BooleanField(default=False, help_text='Show prominently in media section')
    external_publication = models.BooleanField(default=True, help_text='Is this from an external publication?')
    
    # Display Settings
    is_active = models.BooleanField(default=True, help_text='Display this article in the slider')
    display_order = models.IntegerField(default=0, help_text='Order in which articles appear (lower numbers first)')
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    
    # Internal tracking
    clicks_count = models.IntegerField(default=0, help_text='Number of times this article link was clicked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['display_order', '-publication_date']
        verbose_name = 'Media Coverage Article'
        verbose_name_plural = 'Media Coverage Articles'
    
    def __str__(self):
        return f"{self.title} - {self.publication}"
    
    def get_short_description(self):
        """Return truncated description for display"""
        return self.description[:250] + "..." if len(self.description) > 250 else self.description
    
    def get_icon_class(self):
        """Return the full FontAwesome class"""
        return f"fas {self.icon}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
