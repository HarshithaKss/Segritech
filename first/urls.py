from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('solutions/', views.solutions, name='solutions'),
    path('careers/', views.careers, name='careers'),
    path('careers/job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('careers/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('faq/', views.faq_page, name='faq_page'),
    path('faq-section/', views.faq_section, name='faq_section'),
    
    # Products URLs
    path('products/', views.products, name='products'),
    path('products/<slug:category_slug>/', views.category_products, name='category_products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('api/product-inquiry/', views.product_inquiry, name='product_inquiry'),
    
    # Legacy category URLs (keep for backward compatibility)
    path('products/size-graders/', views.size_graders, name='size_graders'),
    path('products/quality-graders/', views.quality_graders, name='quality_graders'),
    path('products/weight-graders/', views.weight_graders, name='weight_graders'),
    path('products/cleaning-machines/', views.cleaning_machines, name='cleaning_machines'),
    path('products/packing-robots/', views.packing_robots, name='packing_robots'),
    
    # Latest Technology URLs
    path('inspection-box/', views.inspection_box, name='inspection_box'),
    path('send-inquiry/', views.send_inquiry, name='send_inquiry'),
    path('newsletter/signup/', views.newsletter_signup, name='newsletter_signup'),
    
    # Blog URLs - Now Active!
    path('insights/', views.blog_list, name='blog_list'),
    path('insights/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
    # Explore Page
    path('explore/', views.explore, name='explore'),
    
    # NEW: Crop Analysis URLs
    path('analyze/potato/', views.analyze_potato, name='analyze_potato'),
    path('analyze/apple/', views.analyze_apple, name='analyze_apple'),
    path('analyze/pomegranate/', views.analyze_pomegranate, name='analyze_pomegranate'),
    path('analyze/orange/', views.analyze_orange, name='analyze_orange'),
    path('analyze/onion/', views.analyze_onion, name='analyze_onion'),
    path('analyze/capsicum/', views.analyze_capsicum, name='analyze_capsicum'),
    path('analyze/tomato/', views.analyze_tomato, name='analyze_tomato'),
    path('analyze/lemon/', views.analyze_lemon, name='analyze_lemon'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)