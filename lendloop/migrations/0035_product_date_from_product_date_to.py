# Generated by Django 4.1.6 on 2024-01-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0034_remove_product_availabilities_delete_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
