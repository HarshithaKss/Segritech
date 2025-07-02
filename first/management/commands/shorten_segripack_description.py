"""
Django management command to shorten SegriPack description to 4-5 important lines.
This command updates the detailed description of SegriPack to be concise and focused.
Compatible with Python 3.7+ and uses simple Django ORM operations.
"""

from django.core.management.base import BaseCommand
from first.models import Product


class Command(BaseCommand):
    help = 'Shorten SegriPack description to 4-5 important lines'

    def handle(self, *args, **options):
        try:
            # Find the SegriPack product
            segripack = Product.objects.filter(name='SegriPack by Segritech').first()
            
            if not segripack:
                self.stdout.write(self.style.ERROR('SegriPack product not found.'))
                return

            # Update with shorter description (4-5 lines)
            segripack.detailed_description = '''SegriPack by Segritech - Smart Robotic Packing System for Graded Fresh Produce

SegriPack is Segritech's flagship automated packaging solution designed specifically for graded fresh produce. This intelligent robotic system combines precision handling with smart weighing technology to deliver consistent, retail-ready packaging.

Built for Indian agricultural operations, SegriPack offers the perfect balance of automation, reliability, and cost-effectiveness. Whether you're packaging pomegranates, apples, citrus fruits, or other fresh produce, SegriPack ensures professional presentation while reducing labor dependency.

Smart robotic arms with gentle produce handling, integrated precision weighing, and multi-format packaging capability make it ideal for modern agricultural packaging needs.'''

            # Save the updated product
            segripack.save()

            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully shortened SegriPack description to 4-5 important lines'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating SegriPack description: {str(e)}')
            ) 