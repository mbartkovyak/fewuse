import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from lendloop.models import Product

def random_date(start, end):
    """Generate a random date between `start` and `end`."""
    return start + timedelta(days=random.randint(0, (end - start).days))

class Command(BaseCommand):
    help = 'Populate date_from and date_to for products'

    def handle(self, *args, **options):
        products = Product.objects.all()
        start_date = date(2023, 1, 1)
        end_date = date(2024, 12, 31)

        for product in products:
            date_from = random_date(start_date, end_date)
            # Ensure date_to is after date_from
            date_to = random_date(date_from, end_date)

            product.date_from = date_from
            product.date_to = date_to
            product.save()

            self.stdout.write(self.style.SUCCESS(f'Updated product {product.name} with dates {date_from} - {date_to}'))
