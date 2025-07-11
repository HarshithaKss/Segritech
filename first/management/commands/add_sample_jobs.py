from django.core.management.base import BaseCommand
from first.models import JobPosting
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Add sample job postings'

    def handle(self, *args, **options):
        # Sample job postings data
        jobs_data = [
            {
                'title': 'Mechanical Engineer',
                'department': 'engineering',
                'job_type': 'full_time',
                'experience_level': 'mid',
                'location': 'Bangalore, India',
                'remote_allowed': False,
                'description': 'We are looking for a skilled Mechanical Engineer to join our R&D team...',
                'responsibilities': '''
- Design and develop mechanical components for agricultural machinery
- Create detailed 3D models and technical drawings using CAD software
- Collaborate with cross-functional teams to optimize product designs
- Conduct structural and thermal analyses
- Oversee prototyping and testing of new designs
                ''',
                'requirements': '''
- B.Tech/M.Tech in Mechanical Engineering
- 3-5 years experience in product development
- Proficiency in SolidWorks or similar CAD software
- Strong understanding of GD&T and manufacturing processes
- Experience with agricultural machinery is a plus
                ''',
                'nice_to_have': '''
- Experience with automation systems
- Knowledge of IoT and sensor integration
- Familiarity with rapid prototyping technologies
                ''',
                'benefits': '''
- Competitive salary package
- Health insurance for self and family
- Professional development opportunities
- Flexible work hours
- Stock options
                ''',
                'salary_min': 1000000,
                'salary_max': 1800000,
                'equity_offered': True,
                'deadline': timezone.now().date() + timedelta(days=30),
                'is_active': True
            },
            {
                'title': 'Mechatronics Internship',
                'department': 'engineering',
                'job_type': 'internship',
                'experience_level': 'entry',
                'location': 'Bangalore, India',
                'remote_allowed': False,
                'description': 'Join our innovative team as a Mechatronics Intern...',
                'responsibilities': '''
- Assist in the development of automated systems
- Work on integration of sensors and actuators
- Help with testing and validation of prototypes
- Document technical processes and results
                ''',
                'requirements': '''
- Currently pursuing B.Tech/M.Tech in Mechatronics/Mechanical/Electronics
- Strong foundation in mechanical and electronic systems
- Basic programming skills (Python/Arduino)
- Eager to learn and contribute to real projects
                ''',
                'nice_to_have': '''
- Previous internship experience
- Knowledge of ROS
- Experience with microcontrollers
                ''',
                'benefits': '''
- Stipend based on capabilities
- Certificate upon completion
- Potential for pre-placement offer
- Hands-on experience with cutting-edge technology
                ''',
                'salary_min': 25000,
                'salary_max': 40000,
                'equity_offered': False,
                'deadline': timezone.now().date() + timedelta(days=15),
                'is_active': True
            }
        ]

        # Create job postings
        for job_data in jobs_data:
            JobPosting.objects.get_or_create(
                title=job_data['title'],
                defaults=job_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample job postings')) 