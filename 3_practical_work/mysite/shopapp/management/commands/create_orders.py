from django.core.management.base import BaseCommand
from shopapp.models import Order, Product
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create sample orders'

    def handle(self, *args, **options):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No User found. Run createsuperuser first.'))
            return

        products = list(Product.objects.all())
        if not products:
            self.stdout.write(self.style.ERROR('No products found. Run create_products first.'))
            return

        orders_data = [
            {"address": "123 Lenina St, Omsk"},
            {"address": "456 Pushkina St, Pskov"},
        ]

        for data in orders_data:
            order, created = Order.objects.get_or_create(
                delivery_address=data["address"],
                defaults={"user": user, "promo_code": "SALE10"}
            )
            if created:
                order.products.set(products[:2])
                self.stdout.write(self.style.SUCCESS(f'Created order: {order}'))
            else:
                self.stdout.write(f'Order exists: {order}')
