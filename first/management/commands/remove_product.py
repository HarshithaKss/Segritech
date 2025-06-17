from django.core.management.base import BaseCommand
from first.models import Product

class Command(BaseCommand):
    help = 'Remove a specific product by name'

    def add_arguments(self, parser):
        parser.add_argument('product_name', type=str, help='Name of the product to remove')

    def handle(self, *args, **options):
        product_name = options['product_name']
        try:
            product = Product.objects.get(name=product_name)
            product.delete()
            self.stdout.write(
                self.style.SUCCESS(f'Successfully removed product: {product_name}')
            )
        except Product.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Product not found: {product_name}')
            ) 