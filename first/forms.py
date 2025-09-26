from django import forms
from .models import Contact, JobApplication, ProductInquiry
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'company', 'inquiry_type', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your company name'
            }),
            'inquiry_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the subject of your inquiry',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message here...',
                'rows': 5,
                'required': True
            }),

        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        job_posting = self.instance.job_posting if hasattr(self.instance, 'job_posting') else None
        
        if job_posting and JobApplication.objects.filter(job_posting=job_posting, email=email).exists():
            raise forms.ValidationError('You have already applied for this position.')
        
        return email

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'current_location', 
            'willing_to_relocate', 'current_company', 'current_role', 'years_experience',
            'resume', 'cover_letter', 'portfolio_url', 'expected_salary', 
            'earliest_start_date', 'visa_sponsorship_required',
            'reference1_name', 'reference1_email', 'reference1_phone', 'reference1_relation'
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'required': True
            }),
            'current_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Bangalore, India',
                'required': True
            }),
            'willing_to_relocate': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'current_company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Current company name'
            }),
            'current_role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Current job title'
            }),
            'years_experience': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
                'required': True
            }),
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us why you want to join SegriTech and how you can contribute to our mission...',
                'rows': 6,
                'required': True
            }),
            'portfolio_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://your-portfolio.com or LinkedIn profile'
            }),
            'expected_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Expected salary per annum (INR)',
                'min': '0'
            }),
            'earliest_start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'visa_sponsorship_required': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'reference1_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reference name'
            }),
            'reference1_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reference email'
            }),
            'reference1_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reference phone'
            }),
            'reference1_relation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Previous Manager, Colleague'
            }),
        }
    
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if resume.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError('Resume file size should not exceed 5MB.')
            
            # Check file extension
            allowed_extensions = ['.pdf', '.doc', '.docx']
            file_extension = resume.name.lower().split('.')[-1]
            if f'.{file_extension}' not in allowed_extensions:
                raise forms.ValidationError('Please upload resume in PDF, DOC, or DOCX format.')
        
        return resume

    def clean_earliest_start_date(self):
        from datetime import date
        start_date = self.cleaned_data.get('earliest_start_date')
        
        if start_date:
            # Check if date is not in the past
            if start_date < date.today():
                raise forms.ValidationError('Start date cannot be in the past.')
            
            # Check if date is not too far in the future (e.g., within next 2 years)
            max_future_date = date.today().replace(year=date.today().year + 2)
            if start_date > max_future_date:
                raise forms.ValidationError('Start date cannot be more than 2 years in the future.')
        
        return start_date

class JobFilterForm(forms.Form):
    DEPARTMENT_CHOICES = [('', 'All Departments')] + JobApplication._meta.get_field('job_posting').related_model.DEPARTMENT_CHOICES
    JOB_TYPE_CHOICES = [('', 'All Types')] + JobApplication._meta.get_field('job_posting').related_model.JOB_TYPE_CHOICES
    EXPERIENCE_CHOICES = [('', 'All Levels')] + JobApplication._meta.get_field('job_posting').related_model.EXPERIENCE_LEVEL_CHOICES
    
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search jobs by title or keywords...'
        })
    )
    
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    job_type = forms.ChoiceField(
        choices=JOB_TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    experience_level = forms.ChoiceField(
        choices=EXPERIENCE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    remote_allowed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class ProductInquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = ProductInquiry
        fields = ['name', 'email', 'phone', 'company', 'inquiry_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your company name (Optional)'
            }),
            'inquiry_type': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please describe your requirements and any specific questions...',
                'rows': 4,
                'required': True
            }),
        } 