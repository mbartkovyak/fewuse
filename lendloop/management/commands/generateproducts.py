import random
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lendloop.models import Product, Category, Tag, Location, Ranking, Availability

# Predefined lists (update these lists as per your requirement)
product_names = [
    "Laptop", "Smartphone", "Headphones", "Smartwatch", "Camera",
    "Tablet", "Speaker", "Mouse", "Keyboard", "Monitor",
    "Backpack", "Water Bottle", "Notebook", "Pen", "Desk Lamp",
    "Sunglasses", "Wallet", "Belt", "Hat", "Scarf",
    "Wristband", "Earbuds", "Charger", "HDMI Cable", "Router",
    "Flash Drive", "Memory Card", "Power Bank", "Printer", "Scanner"
]

category_names = ["Electronics", "Accessories", "Stationery", "Wearables", "Computer Peripherals"]

product_descriptions = [
    "High-performance laptop with latest features", "Latest model smartphone with advanced technology",
    "High-quality sound headphones", "Smartwatch with various health tracking features",
    "High-resolution digital camera", "Portable and powerful tablet",
    "Wireless speaker with excellent sound quality", "Ergonomic computer mouse",
    "Mechanical keyboard with backlight", "High-definition computer monitor",
    "Durable and stylish backpack", "Eco-friendly reusable water bottle",
    "Premium quality notebook", "Smooth-writing pen", "Adjustable desk lamp",
    "Fashionable sunglasses", "Leather wallet", "Stylish and durable belt",
    "Comfortable hat", "Warm and cozy scarf",
    "Fitness wristband", "Compact and powerful earbuds",
    "Fast-charging USB charger", "High-speed HDMI cable", "Wireless router with wide coverage",
    "High-capacity USB flash drive", "Reliable memory card", "Portable power bank",
    "Multifunctional printer", "High-speed document scanner"
]

def insert_products(products, tags, locations, availabilities):
    for product in products:
        category_name = product["category"]
        category, _ = Category.objects.get_or_create(name=category_name)

        location = random.choice(locations)
        product_tags = random.sample(tags, 2)  # Select 2 random tags
        product_availabilities = random.sample(availabilities, min(len(availabilities), 3))  # Select up to 3 random availabilities

        product_instance = Product.objects.create(
            name=product["name"],
            user=product["user"],
            created_at=product["created_at"],
            price=product["price"],
            description=product["description"],
            category=category,
            location=location
        )

        product_instance.tags.set(product_tags)
        product_instance.availabilities.set(product_availabilities)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Assuming there are some users in the database
        users = list(User.objects.all())
        if not users:
            print("No users found in the database.")
            return

        # Fetching tags, locations, and availabilities
        tags = list(Tag.objects.all())
        locations = list(Location.objects.all())
        availabilities = list(Availability.objects.all())

        products = []
        for i, product_name in enumerate(product_names):
            category_name = random.choice(category_names)
            description = product_descriptions[i]
            user = random.choice(users)
            products.append({
                "name": product_name,
                "user": user,
                "created_at": date.today(),
                "price": round(random.uniform(10, 500), 2),
                "description": description,
                "category": category_name,
            })

        insert_products(products, tags, locations, availabilities)

