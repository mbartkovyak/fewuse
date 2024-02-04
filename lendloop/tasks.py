from fewuse.celery import app
import logging
from google_sheets.service import write_to_sheet
from lendloop.models import Product, Order
from django.utils import timezone
from datetime import timedelta



#from telegram.client import send_message

"""@app.task(bind=True)
def order_created_task(self, order_id):
    order = Order.objects.select_related('user').prefetch_related('order_products__product', 'order_products__insurance').get(id=order_id)

    message = f"Hi! Thanks for you order!\nYour order id is: {order_id} \n"
    total_price = 0

    for order_product in order.order_products.all():

        product_cost = order_product.product.price * order_product.number_of_days

        # Add insurance cost if applicable
        insurance_cost = order_product.insurance.cost if order_product.insurance else 0
        total_item_cost = product_cost + insurance_cost* order_product.number_of_days
        total_price += total_item_cost

        message += f'You ordered {order_product.product.name}\n' \
                   f'Product Cost: for {order_product.number_of_days} days is {product_cost},\n' \
                   f'Insurance Cost: for {order_product.number_of_days} days is {insurance_cost},\n' \
                   f'Total cost is {total_item_cost}\n'

    message += f'User : {order.user.id}'


    send_message(message)"""


from django.core.mail import send_mail
'''
@app.task(bind=True)
def order_created_task(self, order_id):
    order = Order.objects.select_related('user').prefetch_related('order_products__product', 'order_products__insurance').get(id=order_id)

    message = f"Hi! Thanks for you order!\nYour order id is: {order_id} \n"
    total_price = 0

    for order_product in order.order_products.all():

        product_cost = order_product.product.price * order_product.number_of_days

        # Add insurance cost if applicable
        insurance_cost = order_product.insurance.cost if order_product.insurance else 0
        total_item_cost = product_cost + insurance_cost* order_product.number_of_days
        total_price += total_item_cost

        message += f'You ordered {order_product.product.name}\n' \
                   f'Product Cost: for {order_product.number_of_days} days is {product_cost},\n' \
                   f'Insurance Cost: for {order_product.number_of_days} days is {insurance_cost},\n' \
                   f'Total cost is {total_item_cost}\n'

    message += f'User : {order.user.id}'


    send_mail(
        "New Order",
        message,
        "mbartkovyak@gmail.com",
        [order.user.email],
    )
'''


@app.task(bind=True)
def order_created_task(self, order_id):
    order = Order.objects.select_related('user').prefetch_related('order_products__product', 'order_products__insurance').get(id=order_id)

    message = f"Hi! Thanks for you order!\nYour order id is: {order_id} \n"
    total_price = 0

    for order_product in order.order_products.all():

        product_cost = order_product.product.price * order_product.number_of_days

        # Add insurance cost if applicable
        insurance_cost = order_product.insurance.cost if order_product.insurance else 0
        total_item_cost = product_cost + insurance_cost* order_product.number_of_days
        total_price += total_item_cost

        message += f'You ordered {order_product.product.name}\n' \
                   f'Product Cost: for {order_product.number_of_days} days is {product_cost},\n' \
                   f'Insurance Cost: for {order_product.number_of_days} days is {insurance_cost},\n' \
                   f'Total cost is {total_item_cost}\n'

    message += f'User : {order.user.id}'

    from django.template.loader import render_to_string

    html_message = render_to_string('order_email_template.html', {
        'order_id': order_id,
        'order_products': [
            {
                'product': order_product.product,
                'number_of_days': order_product.number_of_days,
                'product_cost': product_cost,
                'insurance_cost': insurance_cost,
                'total_item_cost': total_item_cost,
            }
            for order_product in order.order_products.all()
        ],
        'user_id': order.user.id,
    })

    send_mail(
        "New Order",
        message,
        "mbartkovyak@gmail.com",
        [order.user.email],
        html_message=html_message
    )


@app.task(bind=True)
def every_day_task(self):

    product_data = []
    yesterday = timezone.now().date() - timedelta(days=1)
    products_created_yesterday = Product.objects.filter(created_at=yesterday)
    for product in products_created_yesterday:
        product_data.append([product.id, product.name, product.price])

    print(product_data)
    write_to_sheet(product_data)

    return "every_day_task is executed"

