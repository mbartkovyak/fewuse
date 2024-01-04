# Generated by Django 4.1.6 on 2024-01-03 18:43

from django.db import migrations, models
import lendloop.models.product


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('price', models.FloatField(validators=[lendloop.models.product.non_negative_validator])),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
