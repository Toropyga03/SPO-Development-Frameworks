from django.core.management.base import BaseCommand
from shopapp.models import Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create sample products'

    def handle(self, *args, **options):
        products_data = [
            {"name": "Laptop", "description": "Powerful laptop", "price": Decimal("999.99"), "stock": 10},
            {"name": "Mouse", "description": "Wireless mouse", "price": Decimal("29.99"), "stock": 50},
            {"name": "Keyboard", "description": "Mechanical keyboard", "price": Decimal("79.99"), "stock": 30},
        ]
        for data in products_data:
            product, created = Product.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "stock": data["stock"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(f'Product exists: {product.name}')
