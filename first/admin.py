from django.contrib import admin
from .models import Contact, JobPosting, JobApplication, ProductCategory, Product, ProductInquiry, BlogPost, Testimonial, MediaCoverageArticle, NewsletterSubscriber

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'inquiry_type', 'subject', 'created_at', 'is_read']
    list_filter = ['inquiry_type', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'company']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Inquiry Details', {
            'fields': ('inquiry_type', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'display_order', 'is_active', 'created_at']
    list_filter = ['category_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['display_order', 'is_active']
    ordering = ['display_order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category_type', 'icon')
        }),
        ('Content', {
            'fields': ('short_description', 'description', 'image')
        }),
        ('Settings', {
            'fields': ('is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_range', 'is_available', 'is_featured', 'display_order', 'created_at']
    list_filter = ['category', 'is_available', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'short_description', 'detailed_description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_available', 'is_featured', 'display_order']
    ordering = ['category', 'display_order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug')
        }),
        ('Content', {
            'fields': ('short_description', 'detailed_description', 'main_image')
        }),
        ('Technical Specifications', {
            'fields': ('specifications', 'dimensions', 'weight', 'power_requirements', 'capacity'),
            'classes': ('collapse',)
        }),
        ('Features & Benefits', {
            'fields': ('key_features', 'applications', 'benefits'),
            'classes': ('collapse',)
        }),
        ('Media & Documents', {
            'fields': ('gallery_images', 'video_url', 'brochure'),
            'classes': ('collapse',)
        }),
        ('Pricing & Availability', {
            'fields': ('price_range', 'is_available', 'lead_time')
        }),
        ('SEO & Meta', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    actions = ['mark_as_featured', 'unmark_as_featured', 'mark_as_available', 'mark_as_unavailable']
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} products marked as featured.')
    mark_as_featured.short_description = "Mark selected products as featured"
    
    def unmark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} products unmarked as featured.')
    unmark_as_featured.short_description = "Unmark selected products as featured"
    
    def mark_as_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f'{updated} products marked as available.')
    mark_as_available.short_description = "Mark selected products as available"
    
    def mark_as_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f'{updated} products marked as unavailable.')
    mark_as_unavailable.short_description = "Mark selected products as unavailable"


@admin.register(ProductInquiry)
class ProductInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'product', 'inquiry_type', 'created_at', 'is_responded']
    list_filter = ['inquiry_type', 'is_responded', 'created_at', 'product__category']
    search_fields = ['name', 'email', 'company', 'product__name', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_responded']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Inquiry Information', {
            'fields': ('product', 'inquiry_type', 'is_responded')
        }),
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Timestamp', {
            'fields': ('created_at',)
        }),
    )


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'job_type', 'experience_level', 'location', 'applications_count', 'is_active', 'is_featured', 'created_at']
    list_filter = ['department', 'job_type', 'experience_level', 'is_active', 'is_featured', 'remote_allowed', 'created_at']
    search_fields = ['title', 'description', 'requirements']
    readonly_fields = ['created_at', 'updated_at', 'applications_count']
    list_editable = ['is_active', 'is_featured']
    ordering = ['-is_featured', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'department', 'job_type', 'experience_level', 'location', 'remote_allowed')
        }),
        ('Job Details', {
            'fields': ('description', 'responsibilities', 'requirements', 'nice_to_have', 'benefits')
        }),
        ('Compensation', {
            'fields': ('salary_min', 'salary_max', 'equity_offered')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured', 'deadline')
        }),
        ('Statistics', {
            'fields': ('applications_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_active', 'mark_as_inactive', 'mark_as_featured', 'unmark_as_featured']
    
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} job postings marked as active.')
    mark_as_active.short_description = "Mark selected jobs as active"
    
    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} job postings marked as inactive.')
    mark_as_inactive.short_description = "Mark selected jobs as inactive"
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} job postings marked as featured.')
    mark_as_featured.short_description = "Mark selected jobs as featured"
    
    def unmark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} job postings unmarked as featured.')
    unmark_as_featured.short_description = "Unmark selected jobs as featured"


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'job_posting', 'years_experience', 'current_location', 'status', 'applied_at']
    list_filter = ['status', 'years_experience', 'willing_to_relocate', 'visa_sponsorship_required', 'applied_at', 'job_posting__department']
    search_fields = ['first_name', 'last_name', 'email', 'current_company', 'current_role', 'job_posting__title']
    readonly_fields = ['applied_at', 'updated_at']
    list_editable = ['status']
    ordering = ['-applied_at']
    
    fieldsets = (
        ('Job Information', {
            'fields': ('job_posting', 'status')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'current_location', 'willing_to_relocate')
        }),
        ('Professional Information', {
            'fields': ('current_company', 'current_role', 'years_experience', 'expected_salary', 'earliest_start_date')
        }),
        ('Application Materials', {
            'fields': ('resume', 'cover_letter', 'portfolio_url')
        }),
        ('Additional Information', {
            'fields': ('visa_sponsorship_required',)
        }),
        ('References', {
            'fields': ('reference1_name', 'reference1_email', 'reference1_phone', 'reference1_relation'),
            'classes': ('collapse',)
        }),
        ('Internal Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('applied_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['mark_as_under_review', 'mark_as_shortlisted', 'mark_as_rejected']
    
    def mark_as_under_review(self, request, queryset):
        updated = queryset.update(status='under_review')
        self.message_user(request, f'{updated} applications marked as under review.')
    mark_as_under_review.short_description = "Mark as under review"
    
    def mark_as_shortlisted(self, request, queryset):
        updated = queryset.update(status='shortlisted')
        self.message_user(request, f'{updated} applications shortlisted.')
    mark_as_shortlisted.short_description = "Mark as shortlisted"
    
    def mark_as_rejected(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} applications marked as rejected.')
    mark_as_rejected.short_description = "Mark selected applications as rejected"


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author_name', 'is_published', 'is_featured', 'views_count', 'published_at']
    list_filter = ['category', 'is_published', 'is_featured', 'created_at', 'published_at']
    search_fields = ['title', 'excerpt', 'content', 'author_name', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'is_featured']
    ordering = ['-published_at', '-created_at']
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'excerpt')
        }),
        ('Author Information', {
            'fields': ('author_name', 'author_title', 'author_image')
        }),
        ('Content', {
            'fields': ('content', 'featured_image')
        }),
        ('SEO & Meta', {
            'fields': ('meta_title', 'meta_description', 'tags'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured', 'published_at')
        }),
        ('Statistics', {
            'fields': ('views_count', 'comments_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at', 'views_count']
    
    actions = ['mark_as_published', 'mark_as_unpublished', 'mark_as_featured', 'unmark_as_featured']
    
    def mark_as_published(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(is_published=True, published_at=timezone.now())
        self.message_user(request, f'{updated} blog posts published.')
    mark_as_published.short_description = "Mark selected posts as published"
    
    def mark_as_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} blog posts unpublished.')
    mark_as_unpublished.short_description = "Mark selected posts as unpublished"
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} blog posts marked as featured.')
    mark_as_featured.short_description = "Mark selected posts as featured"
    
    def unmark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} blog posts unmarked as featured.')
    unmark_as_featured.short_description = "Unmark selected posts as featured"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'country', 'impact_metric', 'is_active', 'is_featured', 'display_order', 'created_at']
    list_filter = ['role', 'country', 'is_active', 'is_featured', 'created_at']
    search_fields = ['name', 'company_or_location', 'quote', 'country']
    list_editable = ['is_active', 'is_featured', 'display_order']
    ordering = ['display_order', '-created_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'role', 'company_or_location', 'country', 'photo')
        }),
        ('Testimonial Content', {
            'fields': ('quote', 'impact_metric', 'impact_icon')
        }),
        ('Media', {
            'fields': ('video_url',),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']
    
    actions = ['mark_as_active', 'mark_as_inactive', 'mark_as_featured', 'unmark_as_featured']
    
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} testimonials marked as active.')
    mark_as_active.short_description = "Mark selected testimonials as active"
    
    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} testimonials marked as inactive.')
    mark_as_inactive.short_description = "Mark selected testimonials as inactive"
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} testimonials marked as featured.')
    mark_as_featured.short_description = "Mark selected testimonials as featured"
    
    def unmark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} testimonials unmarked as featured.')
    unmark_as_featured.short_description = "Unmark selected testimonials as featured"


@admin.register(MediaCoverageArticle)
class MediaCoverageArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication', 'category', 'publication_date', 'is_active', 'is_featured', 'display_order', 'clicks_count']
    list_filter = ['category', 'publication', 'is_active', 'is_featured', 'external_publication', 'publication_date', 'created_at']
    search_fields = ['title', 'publication', 'description']
    list_editable = ['is_active', 'is_featured', 'display_order']
    ordering = ['display_order', '-publication_date']
    date_hierarchy = 'publication_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'publication', 'category', 'icon')
        }),
        ('Content', {
            'fields': ('description', 'article_url', 'featured_image')
        }),
        ('Publication Details', {
            'fields': ('publication_date', 'external_publication')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'is_featured', 'display_order')
        }),
        ('SEO & Meta', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('clicks_count',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at', 'clicks_count']
    
    actions = ['mark_as_active', 'mark_as_inactive', 'mark_as_featured', 'unmark_as_featured', 'reset_click_counts']
    
    def mark_as_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} articles marked as active.')
    mark_as_active.short_description = "Mark selected articles as active"
    
    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} articles marked as inactive.')
    mark_as_inactive.short_description = "Mark selected articles as inactive"
    
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} articles marked as featured.')
    mark_as_featured.short_description = "Mark selected articles as featured"
    
    def unmark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} articles unmarked as featured.')
    unmark_as_featured.short_description = "Unmark selected articles as featured"
    
    def reset_click_counts(self, request, queryset):
        updated = queryset.update(clicks_count=0)
        self.message_user(request, f'Click counts reset for {updated} articles.')
    reset_click_counts.short_description = "Reset click counts for selected articles"


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_active')
    list_filter = ('is_active', 'subscribed_at')
    search_fields = ('email',)
    date_hierarchy = 'subscribed_at'
