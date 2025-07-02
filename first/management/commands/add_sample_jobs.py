from django.core.management.base import BaseCommand
from first.models import JobPosting
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Add sample job postings'

    def handle(self, *args, **kwargs):
        # Mechanical Engineer Position
        mechanical_engineer = JobPosting.objects.create(
            title="Mechanical Engineer",
            department="hardware",
            job_type="full_time",
            experience_level="mid",
            location="Hyderabad",
            remote_allowed=False,
            description="""About Segritech:
Segritech is a deep-tech agritech startup focused on transforming the way fruits and vegetables are graded and sorted at the farm level. We design advanced machinery integrated with AI-based computer vision to bring automation and transparency to the agri-value chain.

Role Overview:
We are seeking a passionate and detail-oriented Mechanical Engineer with 3–4 years of experience in designing electro-mechanical systems or agri/industrial machinery. You will be responsible for the end-to-end mechanical design, prototyping, testing, and integration of our fruit-sorting and inspection systems.""",
            responsibilities="""- Lead mechanical design and development of grading/sorting machines
- Work with cross-functional teams (software, electronics, AI) to integrate systems
- Design assemblies, frames, conveyors, and sensor/camera housings using CAD tools (SolidWorks/AutoCAD/Fusion 360)
- Prepare fabrication drawings and BOMs
- Optimize designs for cost, manufacturability, and robustness
- Oversee prototyping, vendor management, and field deployment
- Troubleshoot issues in live environments and implement design improvements""",
            requirements="""- B.E./B.Tech in Mechanical Engineering (M.E./M.Tech is a plus)
- 3–4 years of experience in machine design, preferably in automation, robotics, or agri/packaging equipment
- Proficiency in CAD software (SolidWorks preferred)
- Good understanding of mechanical systems, sheet metal, gear systems, motors, conveyors, and structural analysis
- Exposure to pneumatics, motion systems, and industrial sensors is a plus
- Hands-on approach with a passion for building things from scratch
- Experience with vendor coordination and fabrication processes
- Strong problem-solving and project management skills""",
            nice_to_have="""- Experience working in startups or product development teams
- Familiarity with computer vision or camera integration
- Knowledge of IP ratings, ruggedization for field use, or agricultural applications""",
            benefits="""Be part of a fast-growing deep-tech startup making real-world impact
Work on challenging problems that combine mechanical, AI, and agri-tech
Opportunity to lead and grow with the company as we scale pan-India and globally""",
            salary_min=450000,  # 4.5L
            salary_max=500000,  # 5L
            equity_offered=False,
            is_active=True,
            is_featured=True,
            deadline=timezone.now() + timedelta(days=30)
        )

        # Mechatronics Internship Position
        mechatronics_intern = JobPosting.objects.create(
            title="Mechatronics Internship",
            department="hardware",
            job_type="internship",
            experience_level="entry",
            location="Hyderabad",
            remote_allowed=False,
            description="""Duties Of The Mechatronics Intern:
- Embedded Systems
- 3D modeling of hardware design on Solid Works/Fusion360/blender
- Electronics hardware & PCB Designing
- Working on mechanical design and electronic circuits
- Fabrication and assembly work-stream
- Working on pre-product deployment tests
- Firmware & Programming
- Working on Raspberry Pi/Nvidia Jetson Nano/Arduino
- Python/embedded C programming
- Documentation and release of components for manufacturing
- Coordination with the software team""",
            requirements="""Essential Skills Required:
- Good handson in 3d designing on Solidworks or Fusion360
- Experience on Raspberry Pi and Arduino
- Familiar with ARM/PIC32 processor family
- Experience with communication protocols like UART, CAN, MODBUS, RS232, Ethernet etc
- Experience with PCB designing and debugging
- Self-motivated, problem solver, good communication skills
- Good level of presentation skills (verbal and written)
- Good multi-tasking skills""",
            nice_to_have="""Desirable Skills:
- Knowledge of design in safety critical environments
- Knowledge of ISO 26262
- Knowledge of Raspberry pi
- Knowledge of embedded programming on rpi
- Knowledge of Solid Works""",
            salary_min=5000,
            salary_max=6000,
            equity_offered=False,
            is_active=True,
            is_featured=True,
            deadline=timezone.now() + timedelta(days=30)
        )

        self.stdout.write(self.style.SUCCESS('Successfully added sample job postings')) 