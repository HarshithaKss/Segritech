from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm, JobApplicationForm, JobFilterForm, ProductInquiryForm
from .models import JobPosting, JobApplication, ProductCategory, Product, ProductInquiry, BlogPost, Testimonial, MediaCoverageArticle, NewsletterSubscriber
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def index(request):
    # Get published blog posts for insights section (latest 3)
    blog_posts = BlogPost.objects.filter(is_published=True)[:3]
    
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
            messages.success(request, 'Thank you for your message! We will get back to you within 24 hours.')
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
New inquiry received:

Product: {product}

Customer Details:
Name: {name}
Email: {email}
Phone: {phone}
Company: {company or 'Not provided'}

Message:
{message}
                """
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your inquiry! We will get back to you soon.')
            except Exception as e:
                print(f"Failed to send email: {e}")
                messages.error(request, 'Sorry, there was an error sending your inquiry. Please try again later.')
            
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
            
            messages.success(request, 
                f'Thank you for applying to {job.title}! We will review your application and get back to you soon.')
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

@require_POST
def newsletter_signup(request):
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
