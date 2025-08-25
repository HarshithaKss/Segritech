from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import ContactForm, JobApplicationForm, JobFilterForm, ProductInquiryForm
from .models import JobPosting, JobApplication, ProductCategory, Product, ProductInquiry, BlogPost, Testimonial, MediaCoverageArticle, NewsletterSubscriber, FAQ
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json
# Create your views here.

def index(request):
    """
    View for the homepage
    """
    featured_products = Product.objects.filter(is_featured=True)[:6]
    featured_blogs = BlogPost.objects.filter(is_featured=True)[:3]
    testimonials = Testimonial.objects.all()[:3]
    featured_faqs = FAQ.objects.filter(is_featured=True).order_by('order')[:6]  # Get top 6 featured FAQs
    
    context = {
        'featured_products': featured_products,
        'featured_blogs': featured_blogs,
        'testimonials': testimonials,
        'faqs': featured_faqs,  # Add FAQs to context
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_obj = form.save()  # save to DB first

            # Send email to admin
            send_mail(
                subject=f"New Contact Us Inquiry from {contact_obj.name}",
                message=f"Name: {contact_obj.name}\nEmail: {contact_obj.email}\n\nMessage:\n{contact_obj.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    # Get featured FAQs for the contact page
    featured_faqs = FAQ.objects.filter(is_featured=True).order_by('order')[:6]
    
    return render(request, 'contact.html', {
        'form': form,
        'faqs': featured_faqs,
    })

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
    # Handle redirect for old Multifruit Optical Grader URL
    if category_slug == 'quality-graders' and product_slug == 'multifruit-optical-grader':
        return redirect('product_detail', category_slug='quality-graders', product_slug='segritech-minisort', permanent=True)
    
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
                return JsonResponse({'success': True, 'message': 'Inquiry submitted successfully.'})
            except Exception as e:
                print(f"Failed to send email: {e}")
                return JsonResponse({'success': False, 'message': 'Inquiry saved, but failed to send email.'}, status=500)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
 



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
    form = JobFilterForm(request.GET)
    
    # Base queryset
    jobs = JobPosting.objects.filter(is_active=True)
    
    # Apply filters if form is valid
    if form.is_valid():
        # Search by title or description
        search = form.cleaned_data.get('search')
        if search:
            jobs = jobs.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(requirements__icontains=search)
            )
        
        # Department filter
        department = form.cleaned_data.get('department')
        if department:
            jobs = jobs.filter(department=department)
        
        # Job type filter
        job_type = form.cleaned_data.get('job_type')
        if job_type:
            jobs = jobs.filter(job_type=job_type)
        
        # Experience level filter
        experience_level = form.cleaned_data.get('experience_level')
        if experience_level:
            jobs = jobs.filter(experience_level=experience_level)
        
        # Remote filter
        remote_allowed = form.cleaned_data.get('remote_allowed')
        if remote_allowed:
            jobs = jobs.filter(remote_allowed=True)
    
    # Get department counts for sidebar
    department_counts = JobPosting.objects.filter(is_active=True).values('department').annotate(count=Count('id'))
    
    # Get job type counts for sidebar
    job_type_counts = JobPosting.objects.filter(is_active=True).values('job_type').annotate(count=Count('id'))
    
    context = {
        'jobs': jobs,
        'form': form,
        'department_counts': department_counts,
        'job_type_counts': job_type_counts,
        'total_jobs': jobs.count(),
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

            # Save new application
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

                from django.core.mail import EmailMessage
                email = EmailMessage(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL]
                )
                if application.resume:
                    email.attach(application.resume.name, application.resume.read(), application.resume.content_type)
                email.send(fail_silently=False)

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
SegriTech is a deep-tech agritech startup focused on transforming the way fruits and vegetables are graded and sorted at the farm level.

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
                messages.success(
                    request,
                    f"Thank you for applying to {job.title}! A confirmation email has been sent to {application.email}."
                )

            except Exception as e:
                print(f"Failed to send job application emails: {e}")
                messages.warning(
                    request,
                    f"Thank you for applying to {job.title}! However, we could not send a confirmation email right now."
                )

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



from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import NewsletterSubscriber

def newsletter_signup(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
    email = request.POST.get('email', '').strip()
    
    if not email:
        return JsonResponse({'success': False, 'message': 'Email is required'})
    
    try:
        # Validate email format
        validate_email(email)
        
        # Check if email already exists
        if NewsletterSubscriber.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'message': 'You are already subscribed to our newsletter!'
            })
        
        # Create new subscriber
        NewsletterSubscriber.objects.create(email=email)
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for subscribing to our newsletter!'
        })
        
    except ValidationError:
        return JsonResponse({
            'success': False,
            'message': 'Please enter a valid email address'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
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

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def faq_section(request):
    """
    View for the homepage FAQ section that shows only featured questions
    """
    featured_faqs = FAQ.objects.filter(is_featured=True)
    return render(request, 'faq_section.html', {'faqs': featured_faqs})

def faq_page(request):
    """
    View for the full FAQ page that shows all questions
    """
    all_faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': all_faqs})
