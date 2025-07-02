from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import ContactForm, JobApplicationForm, JobFilterForm, ProductInquiryForm
from .models import JobPosting, JobApplication, ProductCategory, Product, ProductInquiry, BlogPost, Testimonial, MediaCoverageArticle, NewsletterSubscriber
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json

# Create your views here.

def index(request):
    # Get featured blog posts for insights section (max 3)
    blog_posts = BlogPost.objects.filter(is_published=True, is_featured=True).order_by('-published_at', '-created_at')[:3]
    
    # Get active testimonials for testimonials section
    testimonials = Testimonial.objects.filter(is_active=True)
    
    # Get active media coverage articles for media section
    media_articles = MediaCoverageArticle.objects.filter(is_active=True)
    
    context = {
        'blog_posts': blog_posts,
        'testimonials': testimonials,
        'media_articles': media_articles,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            
            # Send email notification to admin
            try:
                subject = f'New Contact Form Submission: {contact_submission.subject}'
                email_message = f"""
New contact form submission received:

Name: {contact_submission.name}
Email: {contact_submission.email}
Phone: {contact_submission.phone or 'Not provided'}
Company: {contact_submission.company or 'Not provided'}
Inquiry Type: {contact_submission.get_inquiry_type_display()}
Subject: {contact_submission.subject}

Message:
{contact_submission.message}

Submitted at: {contact_submission.created_at}
                """
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, f'Thank you, {contact_submission.name}! Your message has been received. Our team will get back to you within 24 hours.')
            except Exception as e:
                print(f"Failed to send contact form email: {e}")
                # Still show success message to user, but log the error
                messages.success(request, f'Thank you, {contact_submission.name}! Your message has been received. Our team will get back to you within 24 hours.')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def team(request):
    return render(request, 'team.html')

# Product views
def products(request):
    """Main products page showing all categories"""
    categories = ProductCategory.objects.filter(is_active=True)
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    
    context = {
        'categories': categories,
        'featured_products': featured_products,
    }
    return render(request, 'products.html', context)

def size_graders(request):
    """Size Graders category page"""
    category = get_object_or_404(ProductCategory, category_type='size_graders', is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def quality_graders(request):
    """Quality Graders category page"""
    category = get_object_or_404(ProductCategory, category_type='quality_graders', is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def weight_graders(request):
    """Weight Graders category page"""
    category = get_object_or_404(ProductCategory, category_type='weight_graders', is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def cleaning_machines(request):
    """Cleaning Machines category page"""
    category = get_object_or_404(ProductCategory, category_type='cleaning_machines', is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def packing_robots(request):
    """Packing Robots category page"""
    category = get_object_or_404(ProductCategory, category_type='packing_robots', is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def category_products(request, category_slug):
    """Generic category page that handles all categories by slug"""
    category = get_object_or_404(ProductCategory, slug=category_slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    context = {
        'category': category,
        'products': products,
        'other_categories': other_categories,
    }
    return render(request, 'product_category.html', context)

def product_detail(request, category_slug, product_slug):
    """Individual product detail page"""
    category = get_object_or_404(ProductCategory, slug=category_slug, is_active=True)
    product = get_object_or_404(Product, slug=product_slug, category=category, is_active=True)
    related_products = Product.objects.filter(category=category, is_active=True).exclude(id=product.id)[:3]
    other_categories = ProductCategory.objects.filter(is_active=True).exclude(id=category.id)
    
    # Initialize the inquiry form
    inquiry_form = ProductInquiryForm()
    
    context = {
        'product': product,
        'category': category,
        'related_products': related_products,
        'other_categories': other_categories,
        'inquiry_form': inquiry_form,
    }
    return render(request, 'product_detail.html', context)

@csrf_exempt
def product_inquiry(request):
    """Handle product inquiry form submission via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            
            # Get the product
            product = get_object_or_404(Product, id=product_id)
            
            # Create the inquiry
            inquiry = ProductInquiry.objects.create(
                product=product,
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                company=data.get('company', ''),
                inquiry_type=data.get('inquiry_type'),
                message=data.get('message')
            )
            
            # Send email to admin
            try:
                subject = f'New Product Inquiry: {product.name}'
                message = f"""
New product inquiry received:

Product: {product.name}
Category: {product.category.name}

Customer Details:
Name: {inquiry.name}
Email: {inquiry.email}
Phone: {inquiry.phone}
Company: {inquiry.company or 'Not provided'}
Inquiry Type: {inquiry.get_inquiry_type_display()}

Message:
{inquiry.message}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email: {e}")
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def inspection_box(request):
    """Inspection Box product page"""
    return render(request, 'inspection_box.html')

@csrf_exempt
def send_inquiry(request):
    """Handle inquiry form submission from the Inspection Box page"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            company = request.POST.get('company', '')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            product = request.POST.get('product')
            
            # Validate required fields
            if not all([name, email, phone, message, product]):
                messages.error(request, 'Please fill in all required fields.')
                return redirect('inspection_box')
            
            # Send email to admin
            try:
                subject = f'New Inquiry: {product}'
                email_message = f"""
New inquiry received from Inspection Box page:

Product: {product}

Customer Details:
Name: {name}
Email: {email}
Phone: {phone}
Company: {company or 'Not provided'}

Message:
{message}

Submitted at: {timezone.now()}
                """
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                print(f"Inquiry email sent successfully for {product} to {settings.ADMIN_EMAIL}")
                messages.success(request, f'Thank you, {name}! Your inquiry about the {product} has been received. We will reach out to you soon.')
            except Exception as e:
                print(f"Failed to send inquiry email: {e}")
                print(f"Email settings - Host: {settings.EMAIL_HOST}, User: {settings.EMAIL_HOST_USER}")
                # Still show success to user but log the error for debugging
                messages.success(request, f'Thank you, {name}! Your inquiry about the {product} has been received. We will reach out to you soon.')
            
            return redirect('inspection_box')
        except Exception as e:
            print(f"Error processing inquiry: {e}")
            messages.error(request, 'Sorry, there was an error processing your inquiry. Please try again.')
            return redirect('inspection_box')
    
    messages.error(request, 'Invalid request method.')
    return redirect('inspection_box')

def solutions(request):
    return render(request, 'solutions.html')

def careers(request):
    # Get filter form
    filter_form = JobFilterForm(request.GET)
    
    # Start with active job postings
    jobs = JobPosting.objects.filter(is_active=True)
    
    # Apply filters
    if filter_form.is_valid():
        search = filter_form.cleaned_data.get('search')
        department = filter_form.cleaned_data.get('department')
        job_type = filter_form.cleaned_data.get('job_type')
        experience_level = filter_form.cleaned_data.get('experience_level')
        remote_allowed = filter_form.cleaned_data.get('remote_allowed')
        
        if search:
            jobs = jobs.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(requirements__icontains=search)
            )
        
        if department:
            jobs = jobs.filter(department=department)
        
        if job_type:
            jobs = jobs.filter(job_type=job_type)
        
        if experience_level:
            jobs = jobs.filter(experience_level=experience_level)
        
        if remote_allowed:
            jobs = jobs.filter(remote_allowed=True)
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get some stats for the page
    stats = {
        'total_jobs': JobPosting.objects.filter(is_active=True).count(),
        'internships': JobPosting.objects.filter(is_active=True, job_type='internship').count(),
        'full_time': JobPosting.objects.filter(is_active=True, job_type='full_time').count(),
        'remote': JobPosting.objects.filter(is_active=True, remote_allowed=True).count(),
    }
    
    context = {
        'page_obj': page_obj,
        'filter_form': filter_form,
        'stats': stats,
        'total_jobs': paginator.count,
    }
    
    return render(request, 'careers.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    
    # Get related jobs (same department, excluding current job)
    related_jobs = JobPosting.objects.filter(
        department=job.department,
        is_active=True
    ).exclude(id=job.id)[:3]
    
    context = {
        'job': job,
        'related_jobs': related_jobs,
    }
    
    return render(request, 'job_detail.html', context)

def apply_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_posting = job
            
            # Check for duplicate application
            existing_application = JobApplication.objects.filter(
                job_posting=job,
                email=application.email
            ).first()
            
            if existing_application:
                messages.error(request, 'You have already applied for this position.')
                return redirect('job_detail', job_id=job.id)
            
            application.save()
            
            # Update applications count
            job.applications_count += 1
            job.save()
            
            # Send email notifications
            try:
                # Email to admin/HR team
                admin_subject = f'New Job Application: {job.title} - {application.full_name}'
                admin_message = f"""
New job application received for: {job.title}

Applicant Details:
Name: {application.full_name}
Email: {application.email}
Phone: {application.phone}
Current Location: {application.current_location}
Willing to Relocate: {'Yes' if application.willing_to_relocate else 'No'}

Professional Information:
Current Company: {application.current_company or 'Not provided'}
Current Role: {application.current_role or 'Not provided'}
Years of Experience: {application.get_years_experience_display()}
Expected Salary: {f'₹{application.expected_salary:,} per annum' if application.expected_salary else 'Not specified'}
Earliest Start Date: {application.earliest_start_date}

Cover Letter:
{application.cover_letter}

Portfolio/LinkedIn: {application.portfolio_url or 'Not provided'}

Reference:
{f'{application.reference1_name} ({application.reference1_relation}) - {application.reference1_email}' if application.reference1_name else 'No reference provided'}

Visa Sponsorship Required: {'Yes' if application.visa_sponsorship_required else 'No'}

Applied at: {application.applied_at}

Please review the attached resume and contact the candidate if suitable.
                """
                
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                
                # Confirmation email to applicant
                applicant_subject = f'Application Received: {job.title} at SegriTech'
                applicant_message = f"""
Dear {application.first_name},

Thank you for your interest in the {job.title} position at SegriTech!

We have successfully received your application and our HR team will review it shortly. Here's a summary of your application:

Position Applied For: {job.title}
Department: {job.get_department_display()}
Application Date: {application.applied_at.strftime('%B %d, %Y at %I:%M %p')}

What's Next?
- Our team typically reviews applications within 3-5 business days
- If your profile matches our requirements, we'll contact you to schedule an interview
- You can expect to hear from us within a week

About SegriTech:
SegriTech is a deep-tech agritech startup focused on transforming the way fruits and vegetables are graded and sorted at the farm level. We design advanced machinery integrated with AI-based computer vision to bring automation and transparency to the agri-value chain.

If you have any questions about your application or the position, feel free to reply to this email.

Best regards,
SegriTech HR Team
Email: {settings.ADMIN_EMAIL}
Website: https://segritech.co.in

---
This is an automated confirmation. Please do not reply directly to this email.
                """
                
                send_mail(
                    applicant_subject,
                    applicant_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [application.email],
                    fail_silently=False,
                )
                
            except Exception as e:
                print(f"Failed to send job application emails: {e}")
                # Don't fail the application submission if email fails
            
            messages.success(request, 
                f'Thank you for applying to {job.title}! We have sent a confirmation email to {application.email}. Our team will review your application and get back to you soon.')
            return redirect('job_detail', job_id=job.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobApplicationForm()
    
    context = {
        'job': job,
        'form': form,
    }
    
    return render(request, 'apply_job.html', context)

def newsletter_signup(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
        
    print("Newsletter signup view called")  # Debug log
    email = request.POST.get('email')
    print(f"Received email: {email}")  # Debug log
    
    if not email:
        return JsonResponse({'success': False, 'message': 'Email is required'})
    
    try:
        # Validate email format
        validate_email(email)
        print(f"Email validation passed for: {email}")  # Debug log
        
        # Check if email already exists
        if NewsletterSubscriber.objects.filter(email=email).exists():
            print(f"Email already exists: {email}")  # Debug log
            return JsonResponse({
                'success': False,
                'message': 'You are already subscribed to our newsletter!'
            })
        
        # Create new subscriber
        subscriber = NewsletterSubscriber.objects.create(email=email)
        print(f"Created new subscriber: {subscriber.id}")  # Debug log
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for subscribing to our newsletter!'
        })
        
    except ValidationError:
        print(f"Email validation failed for: {email}")  # Debug log
        return JsonResponse({
            'success': False,
            'message': 'Please enter a valid email address'
        })
    except Exception as e:
        print(f"Unexpected error: {str(e)}")  # Debug log
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        })

def blog_list(request):
    """Display all published blog posts with pagination"""
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-published_at', '-created_at')
    
    # Pagination
    paginator = Paginator(blog_posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_posts': paginator.count,
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, slug):
    """Display individual blog post"""
    blog_post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # If the post has an external URL but we want to display it internally,
    # we can still show the internal content. The external URL can be shown
    # as a "Read Original Article" link if needed.
    
    # Get related posts (same category, excluding current post and specific article)
    related_posts = BlogPost.objects.filter(
        category=blog_post.category,
        is_published=True
    ).exclude(id=blog_post.id).exclude(slug='list-countries-importing-fruit-vegetables-india')[:3]
    
    # Increment views count
    blog_post.views_count += 1
    blog_post.save(update_fields=['views_count'])
    
    context = {
        'blog_post': blog_post,
        'related_posts': related_posts,
    }
    return render(request, 'blog_detail.html', context)

def explore_coming_soon(request):
    """Explore coming soon page with meme GIF"""
    return render(request, 'explore_coming_soon.html')
