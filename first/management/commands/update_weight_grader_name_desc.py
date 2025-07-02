from django.core.management.base import BaseCommand
from first.models import Product

class Command(BaseCommand):
    help = 'Update weight grader description'

    def handle(self, *args, **options):
        try:
            # Find product by current name
            product_name = "Segritech : Weight Grader for Fruits"
            
            product = Product.objects.get(name=product_name)
            
            # Update description - keep existing description and add two more lines
            current_description = product.detailed_description
            additional_lines = (
                " Our weight grader ensures precise sorting based on weight, "
                "making it ideal for export quality standards. "
                "The machine's advanced technology and robust construction guarantee "
                "reliable performance and long-term durability."
            )
            product.detailed_description = current_description + additional_lines
            
            # Save changes
            product.save()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully updated weight grader description'))
            
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Product "{product_name}" not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error updating product: {str(e)}')) 