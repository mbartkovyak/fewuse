# Generated by Django 4.1.6 on 2024-01-17 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0024_remove_rent_product_remove_rent_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='product',
        ),
    ]