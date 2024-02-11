# Generated by Django 4.1.6 on 2024-01-17 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0027_insurance_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='insurance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='lendloop.insurance'),
        ),
    ]
