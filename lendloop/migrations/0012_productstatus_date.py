# Generated by Django 4.1.6 on 2024-01-11 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0011_alter_productstatus_options_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstatus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 23, 49, 24, 134312)),
        ),
    ]