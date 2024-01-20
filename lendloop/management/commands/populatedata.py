import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lendloop.models import Product, Category, Tag, Location, Ranking

# Sample data for each model
category_names = ["Electronics", "Accessories", "Stationery", "Wearables", "Computer Peripherals"]
tag_names = ["New", "Sale", "Popular", "Limited Edition", "Bestseller"]
location_names = ["Boston", "New York", "San Francisco", "Chicago", "Los Angeles"]
ranking_comments = ["Excellent", "Very Good", "Good", "Average", "Below Average"]

product_names = [
    "Laptop", "Smartphone", "Headphones", "Smartwatch", "Camera",
    "Tablet", "Speaker", "Mouse", "Keyboard", "Monitor",
    "Backpack", "Water Bottle", "Notebook", "Pen", "Desk Lamp",
    "Sunglasses", "Wallet", "Belt", "Hat", "Scarf",
    "Wristband", "Earbuds", "Charger", "HDMI Cable", "Router",
    "Flash Drive", "Memory Card", "Power Bank", "Printer", "Scanner"
]

# Sample product descriptions
product_descriptions = [
    "High-performance laptop with the latest features.",
    "Latest model smartphone with advanced technology.",
    "High-quality sound headphones, comfortable for long use.",
    "Smartwatch with health tracking and mobile connectivity.",
    "High-resolution digital camera for professional photography.",
    "Portable and powerful tablet, perfect for work and play.",
    "Wireless speaker with excellent sound quality and durability.",
    "Ergonomic computer mouse, suitable for gaming and office work.",
    "Mechanical keyboard with backlight, ideal for programmers.",
    "High-definition computer monitor with vivid colors.",
    "Durable and stylish backpack, perfect for travel and daily use.",
    "Eco-friendly reusable water bottle, BPA-free and leakproof.",
    "Premium quality notebook for writing and sketching.",
    "Smooth-writing pen with long-lasting ink.",
    "Adjustable desk lamp with different light settings.",
    "Fashionable sunglasses with UV protection.",
    "Leather wallet with multiple compartments.",
    "Stylish and durable belt, made from high-quality materials.",
    "Comfortable and trendy hat, suitable for all seasons.",
    "Warm and cozy scarf, perfect for cold weather.",
    "Fitness wristband with activity tracking and sleep monitoring.",
    "Compact and powerful earbuds with noise cancellation.",
    "Fast-charging USB charger, compatible with multiple devices.",
    "High-speed HDMI cable for optimal audio and video quality.",
    "Wireless router with wide coverage and strong signal.",
    "High-capacity USB flash drive for easy data transfer.",
    "Reliable memory card with fast read/write speeds.",
    "Portable power bank with high battery capacity.",
    "Multifunctional printer for home or office use.",
    "High-speed document scanner with multiple format support."
]


def create_categories():
    for name in category_names:
        Category.objects.get_or_create(name=name, description="Sample description for " + name)

def create_tags():
    for name in tag_names:
        Tag.objects.get_or_create(name=name)

def create_locations():
    for name in location_names:
        Location.objects.get_or_create(location=name)

def create_rankings():
    for i in range(5):
        Ranking.objects.create(stars=i+1, comment=ranking_comments[i])

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def insert_products():
    categories = list(Category.objects.all())
    tags = list(Tag.objects.all())
    locations = list(Location.objects.all())
    rankings = list(Ranking.objects.all())
    users = list(User.objects.all())

    if not users:
        print("No users found in the database.")
        return

    start_date = date(2023, 1, 1)
    end_date = date(2024, 12, 31)

    for i, product_name in enumerate(product_names):
        product_instance = Product.objects.create(
            name=product_name,
            user=random.choice(users),
            created_at=date.today(),
            price=round(random.uniform(10, 500), 2),
            description=product_descriptions[i],
            category=random.choice(categories),
            location=random.choice(locations),
            date_from=random_date(start_date, end_date),
            date_to=random_date(start_date, end_date)
        )

        product_instance.tags.set(random.sample(tags, min(len(tags), 2)))
        product_instance.rankings.set(random.sample(rankings, min(len(rankings), 2)))

class Command(BaseCommand):
    def handle(self, *args, **options):
        create_categories()
        create_tags()
        create_locations()
        create_rankings()
        insert_products()
