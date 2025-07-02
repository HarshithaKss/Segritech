from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Test email configuration by sending a test email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--recipient',
            type=str,
            help='Email address to send test email to (defaults to ADMIN_EMAIL)',
        )

    def handle(self, *args, **options):
        recipient = options.get('recipient') or settings.ADMIN_EMAIL
        
        self.stdout.write(self.style.HTTP_INFO('Testing email configuration...'))
        self.stdout.write(f'Sending test email to: {recipient}')
        
        try:
            result = send_mail(
                subject='Test Email from SegriTech',
                message='This is a test email to verify SMTP configuration is working correctly.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
            
            if result:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Email sent successfully! ({result} message(s) sent)')
                )
            else:
                self.stdout.write(
                    self.style.ERROR('❌ Email sending failed - no messages were sent')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Email sending failed: {str(e)}')
            ) 