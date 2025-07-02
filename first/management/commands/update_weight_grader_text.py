from django.core.management.base import BaseCommand
from first.models import Product

class Command(BaseCommand):
    help = 'Update weight grader description to use new name'

    def handle(self, *args, **options):
        try:
            # Find product by current name
            product_name = "Segritech : Weight Grader for Fruits"
            
            product = Product.objects.get(name=product_name)
            
            # Update description with new name at the start
            new_description = '''The Segritech : Weight Grader for Fruits delivers exceptional accuracy in weight-based grading, essential for export markets requiring strict weight specifications. Features advanced load cells and vibration dampening for consistent results. Our weight grader ensures precise sorting based on weight, making it ideal for export quality standards. The machine's advanced technology and robust construction guarantee reliable performance and long-term durability.'''
            
            product.detailed_description = new_description
            
            # Save changes
            product.save()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully updated weight grader description'))
            
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Product "{product_name}" not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating product: {str(e)}')) 