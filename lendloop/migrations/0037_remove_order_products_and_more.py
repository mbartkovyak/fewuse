# Generated by Django 4.1.6 on 2024-02-04 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0036_alter_product_date_from_alter_product_date_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='number_of_days',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_from',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_to',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='end_date',
            field=models.DateField(default=datetime.date(2025, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 1, 1)),
            preserve_default=False,
        ),
    ]
