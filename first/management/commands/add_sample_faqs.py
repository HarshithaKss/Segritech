"""
Django management command to add sample FAQs to the database.
This command creates initial FAQ entries that will be displayed on the website.
"""

from django.core.management.base import BaseCommand
from first.models import FAQ

class Command(BaseCommand):
    help = 'Adds sample FAQs to the database'

    def handle(self, *args, **options):
        faqs = [
            {
                'question': 'What is Segritech?',
                'answer': 'Segritech is a post-harvest automation company. We use AI and robotics to develop cutting-edge solutions for grading, sorting, inspection, and quality assurance of fruits and vegetables — helping farmers, traders, and exporters reduce losses, improve quality, and scale efficiently.',
                'is_featured': True,
                'order': 1
            },
            {
                'question': 'What is Segritech Minisort?',
                'answer': 'Segritech Minisort is our flagship machine — a compact, portable, AI-powered grader that can sort fruits and vegetables by size, shape, color, and external skin defects. It\'s designed for on-field and farm-level processing, enabling decentralized, high-accuracy grading.',
                'is_featured': True,
                'order': 2
            },
            {
                'question': 'How do I place an order and what is the price range?',
                'answer': 'To place an order:\nChoose your product\n Fill out the form on our website\nOr Call / WhatsApp us at +91 90148 09973\n\nPricing: Machines start from ₹2 Lakhs and go up to ₹20 Lakhs, depending on capacity, crop compatibility, and features.',
                'is_featured': True,
                'order': 3
            },
            {
                'question': 'How do I use the Segritech Minisort?',
                'answer': 'Just plug in the machine, feed the produce through the hopper, and it automatically performs grading and segregation. It has a simple user interface, and our team provides training during installation.',
                'is_featured': True,
                'order': 4
            },
            {
                'question': 'What is the Segritech Inspection Box (SegriBox)?',
                'answer': 'SegriBox is an ultra high-speed, AI-powered inspection unit that analyzes up to 10 fruits per second for color, size, and surface defects. It supports over 15 types of fruits and vegetables, providing real-time data, defect tagging, and grade classification using computer vision.',
                'is_featured': True,
                'order': 5
            },
            {
                'question': 'How can I integrate the Inspection Box with my system?',
                'answer': 'SegriBox is plug-and-play. It connects via USB or LAN, and integrates smoothly with existing conveyor belts, grading lines, ERP systems, and mobile dashboards — enabling analytics, traceability, and remote monitoring.',
                'is_featured': False,
                'order': 6
            },
            {
                'question': 'How does it benefit farmers and local traders?',
                'answer': 'Better prices for uniform, high-quality produce\nSaves time and labor through automation\n✅ Reduces post-harvest losses significantly\n✅ Builds trust and repeat business with buyers',
                'is_featured': False,
                'order': 7
            },
            {
                'question': 'What is the warranty period, and where is service available?',
                'answer': 'We offer a 1-year warranty. Our on-site service network covers all of India, with a typical response time of 24–48 hours in active regions.',
                'is_featured': False,
                'order': 8
            },
            {
                'question': 'What is the lead time for machine installation?',
                'answer': 'Lead time is typically 30–45 days after order confirmation. Our team handles delivery, installation, calibration, and provides hands-on training on-site.',
                'is_featured': False,
                'order': 9
            },
            {
                'question': 'What payment modes do you accept?',
                'answer': 'We accept NEFT, RTGS, Cheques, and standard bank transfers. Payment terms and schedules are shared at the time of quotation.',
                'is_featured': False,
                'order': 10
            },
            {
                'question': 'How does this help the environment?',
                'answer': 'By reducing post-harvest waste, Segritech machines help conserve resources, improve supply chain efficiency, and support climate-smart agriculture and sustainable farming practices.',
                'is_featured': False,
                'order': 11
            },
            {
                'question': 'What is the "Explore" button on the website?',
                'answer': 'The Explore button lets users try out Segritech\'s AI grading demo using their mobile phone camera via browser (and soon through our app). It offers a glimpse into our technology before purchase.',
                'is_featured': False,
                'order': 12
            },
            {
                'question': 'Can I customize the color or design of my machine?',
                'answer': 'Yes. We offer custom colors, stickers, and branding on request — especially for large or institutional orders. Let us know your preferences in advance.',
                'is_featured': False,
                'order': 13
            },
            {
                'question': 'Where can I see a live demo of the machine?',
                'answer': 'Our sales team can share nearby operational locations where our machines are installed. You can schedule a visit to see them in action.',
                'is_featured': False,
                'order': 14
            },
            {
                'question': 'How do I request repairs or replacements?',
                'answer': 'Just call or WhatsApp us, and we will provide remote diagnostics or on-site support as needed. We also offer Annual Maintenance Contracts (AMC) for long-term support.',
                'is_featured': False,
                'order': 15
            },
            {
                'question': 'Is EMI or Buy Now Pay Later available?',
                'answer': 'Yes. We offer EMI plans and deferred payment options through financing partners. These are available to both individuals and institutions.',
                'is_featured': True,
                'order': 6
            },
            {
                'question': 'Is there any government subsidy available for farmers?',
                'answer': 'Yes. Farmers may be eligible for up to 40% subsidy under various state and central government post-harvest schemes. We assist in application and documentation.',
                'is_featured': False,
                'order': 17
            },
            {
                'question': 'What range of products does Segritech offer?',
                'answer': 'We offer a comprehensive portfolio of post-harvest automation solutions:\n\n Size Graders\nMechanical roller-based grading machines for apples, oranges, and other citrus fruits.\n\n✅ Weight Graders (Electronic)\nDigital grading systems based on individual fruit weight. Ideal for pomegranate, apple, orange, mango, dragon fruit, kiwi, avocado, sapota, guava, and more.\n\n✅ AI-Based Quality Grader (Segritech Minisort)\nA smart grader that uses AI to detect size, shape, color, skin texture, and defects — compact and highly accurate for farm-level use.\n\n✅ Inspection Box (SegriBox)\nA standalone, high-speed AI defect inspection unit that integrates easily with existing conveyors and supports 15+ types of fruits and vegetables, including tomato, onion, and potato.\n\n✅ Cleaning Machines\nFor cleaning and waxing of apples, mangoes, oranges, and more — enhances appearance and shelf life.\n\n✅ Packing Robots\nAutomated robotic solutions for fast packaging of apples, oranges, pomegranates, and similar produce — improving speed and hygiene.',
                'is_featured': False,
                'order': 18
            },
            {
                'question': 'Do you offer software or data integration as part of your products?',
                'answer': 'Yes. Most of our machines come with data dashboards, mobile connectivity, and optional cloud sync. We support integration with traceability systems, ERPs, and mobile apps for buyers who want deeper digital insights.',
                'is_featured': False,
                'order': 19
            },
            {
                'question': 'What technical support is available post-purchase?',
                'answer': 'We provide comprehensive technical support including remote diagnostics, on-site maintenance, training for operators, firmware updates, and 24/7 phone support. Our service team covers all major agricultural regions in India.',
                'is_featured': False,
                'order': 20
            },
            {
                'question': 'Can your machines handle different fruit sizes and varieties?',
                'answer': 'Yes, our machines are designed with adjustable parameters to handle various fruit sizes and varieties. For example, our size graders can be configured for different apple varieties (Gala, Fuji, Royal Delicious) and our AI systems can be trained for regional fruit variations.',
                'is_featured': False,
                'order': 21
            },
            {
                'question': 'What is the power consumption and infrastructure requirement?',
                'answer': 'Most machines operate on single-phase or three-phase power (1.5-3 kW typical). Infrastructure requirements are minimal - just a flat surface, power connection, and basic shelter. No special foundations or complex installations required.',
                'is_featured': False,
                'order': 22
            },
            {
                'question': 'Do you provide training for machine operators?',
                'answer': 'Yes, we provide comprehensive training as part of our installation service. This includes hands-on operation training, basic maintenance procedures, troubleshooting, and best practices for optimal results.',
                'is_featured': False,
                'order': 23
            },
            {
                'question': 'What is the typical ROI (Return on Investment) for your machines?',
                'answer': 'Most customers see ROI within 12-18 months through reduced labor costs, improved produce quality leading to better prices, and significant reduction in post-harvest losses. Exact ROI depends on processing volume and current methods.',
                'is_featured': True,
                'order': 24
            },
            {
                'question': 'Can I rent or lease the machines instead of purchasing?',
                'answer': 'Yes, we offer flexible rental and leasing options through our financing partners. This is especially popular for seasonal operations or customers who want to test the technology before making a full purchase.',
                'is_featured': True,
                'order': 25
            },
            {
                'question': 'How accurate are your grading machines?',
                'answer': 'Our machines achieve 95-98% accuracy in grading. AI-based systems (Minisort) achieve even higher accuracy for defect detection. Accuracy can be fine-tuned based on specific grading criteria and quality standards.',
                'is_featured': False,
                'order': 26
            },
            {
                'question': 'What happens if a machine breaks down during peak season?',
                'answer': 'We understand the criticality of peak seasons. We offer priority support during harvest periods, maintain buffer stock of critical components, and can provide temporary replacement units in case of major breakdowns (subject to availability).',
                'is_featured': False,
                'order': 27
            },
            {
                'question': 'Do you offer bulk discounts for multiple machine purchases?',
                'answer': 'Yes, we offer attractive bulk pricing for multiple machine orders, institutional purchases, and FPO (Farmer Producer Organization) orders. Volume discounts start from 2+ machines and increase with order size.',
                'is_featured': False,
                'order': 28
            },
            {
                'question': 'How do I know which machine is right for my operation?',
                'answer': 'Our team provides free consultation to assess your needs based on fruit type, processing volume, quality requirements, budget, and space constraints. We recommend the most suitable solution and can arrange demos before purchase.',
                'is_featured': False,
                'order': 29
            },
            {
                'question': 'Didn\'t find your answer here?',
                'answer': 'We\'re happy to help!\n Call / WhatsApp: +91 90148 09973\n📧 Email: namaste@segritech.com\n🌐 Website: https://segritech.com',
                'is_featured': False,
                'order': 30
            }
        ]

        # First, delete all existing FAQs to avoid duplicates
        FAQ.objects.all().delete()

        for faq_data in faqs:
            FAQ.objects.create(
                question=faq_data['question'],
                answer=faq_data['answer'],
                is_featured=faq_data['is_featured'],
                order=faq_data['order']
            )

        self.stdout.write(self.style.SUCCESS('Successfully added all Segritech FAQs')) 