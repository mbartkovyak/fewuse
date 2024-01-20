import random
from datetime import timedelta, date
from django.core.management.base import BaseCommand
from lendloop.models import Availability  # Replace 'yourapp' with your actual app name


def random_date(start, end):
    """Generate a random date between `start` and `end`."""
    return start + timedelta(days=random.randint(0, (end - start).days))


class Command(BaseCommand):
    help = 'Generates random availability data'

    def handle(self, *args, **options):
        num_availability = 50  # Change this to how many instances you want to create
        start_date = date(2023, 1, 1)  # Start of the date range for generation
        end_date = date(2024, 12, 31)  # End of the date range for generation

        for _ in range(num_availability):
            date_from = random_date(start_date, end_date)
            # Ensure date_to is always after date_from
            date_to = random_date(date_from, end_date)

            Availability.objects.create(date_from=date_from, date_to=date_to)

            self.stdout.write(self.style.SUCCESS(f'Successfully created availability {date_from} to {date_to}'))
