import random
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from lendloop.models import Product, Category, Tag, Location, Ranking

# Predefined lists
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

tag_names = ["New", "Sale", "Popular", "Limited Edition", "Bestseller"]

location_names = ["Boston", "New York", "San Francisco", "Chicago", "Los Angeles"]

def create_tags():
    return [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_names]

def create_locations():
    return [Location.objects.get_or_create(location=location_name)[0] for location_name in location_names]

def create_ranking():
    try:
        stars = round(random.uniform(1, 5), 1)  # Generates a float between 1 and 5, rounded to 1 decimal
        comment = "Sample comment"  # Placeholder comment
        return Ranking.objects.create(stars=stars, comment=comment)
    except ValidationError:
        return None

def insert_products(products, tags, locations):
    for product in products:
        category_name = product["category"]
        category, _ = Category.objects.get_or_create(name=category_name)

        location = random.choice(locations)
        product_tags = random.sample(tags, 2)  # Select 2 random tags

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

        # Create and assign a random ranking
        ranking = create_ranking()
        if ranking:
            product_instance.rankings.add(ranking)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Assuming there are some users in the database
        users = list(User.objects.all())

        if not users:
            print("No users found in the database.")
            return

        tags = create_tags()
        locations = create_locations()

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

        insert_products(products, tags, locations)