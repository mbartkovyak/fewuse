# Generated by Django 4.1.6 on 2024-01-17 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lendloop', '0029_orderproduct_order_products_product_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='insurance',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_insurance', to='lendloop.insurance'),
            preserve_default=False,
        ),
    ]