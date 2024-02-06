from fewuse.celery import app
from google_sheets.service import write_to_sheet
from lendloop.models import Product, Order
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from telegram.client import send_message



@app.task(bind=True)
def order_telegram_created_task(self, order_id):
    order = Order.objects.select_related('user', 'insurance').prefetch_related('order_products__product').get(id=order_id)

    message = f"Hi! Thanks for your order!\nYour order id is: {order_id} \n"
    total_price = 0
    total_insurance_cost = 0  # Initialize total insurance cost

    if order.insurance:
        for order_product in order.order_products.all():
            number_of_days = order_product.rental_period_length()  # Calculate the rental period length
            product_cost = order_product.product.price * number_of_days
            # Calculate the insurance cost once, outside the loop, based on the order-level insurance
            insurance_cost_per_day = order.insurance.cost
            total_item_cost = product_cost
            total_price += total_item_cost

            message += f'You ordered {order_product.product.name}\n' \
                       f'Product Cost: for {number_of_days} days is {product_cost},\n'

        # Calculate total insurance cost based on the entire rental period of all products
        total_days = sum([order_product.rental_period_length() for order_product in order.order_products.all()])
        total_insurance_cost = insurance_cost_per_day * total_days
        total_price += total_insurance_cost

        message += f'Insurance Cost: for all products is {total_insurance_cost},\n'
    else:
        for order_product in order.order_products.all():
            number_of_days = order_product.rental_period_length()
            product_cost = order_product.product.price * number_of_days
            total_item_cost = product_cost
            total_price += total_item_cost

            message += f'You ordered {order_product.product.name}\n' \
                       f'Product Cost: for {number_of_days} days is {product_cost},\n'

    message += f'Total cost is {total_price}\n'
    message += f'User : {order.user.id}'

    send_message(message)


@app.task(bind=True)
def order_created_task(self, order_id):
    order = Order.objects.select_related('user', 'insurance').prefetch_related('order_products__product').get(id=order_id)

    message = f"Hi! Thanks for your order!\nYour order id is: {order_id} \n"
    total_price = 0
    total_insurance_cost = 0  # Initialize total insurance cost

    if order.insurance:
        insurance_cost_per_day = order.insurance.cost
        total_days = 0  # Initialize total rental days

        for order_product in order.order_products.all():
            number_of_days = order_product.rental_period_length()
            product_cost = order_product.product.price * number_of_days
            total_item_cost = product_cost
            total_price += total_item_cost
            total_days += number_of_days

            message += f'You ordered {order_product.product.name}\n' \
                       f'Product Cost: for {number_of_days} days is {product_cost},\n'

        # Calculate total insurance cost based on the total number of rental days
        total_insurance_cost = insurance_cost_per_day * total_days
        total_price += total_insurance_cost

        message += f'Insurance Cost: for all products is {total_insurance_cost},\n'
    else:
        for order_product in order.order_products.all():
            number_of_days = order_product.rental_period_length()
            product_cost = order_product.product.price * number_of_days
            total_item_cost = product_cost
            total_price += total_item_cost

            message += f'You ordered {order_product.product.name}\n' \
                       f'Product Cost: for {number_of_days} days is {product_cost},\n'

    message += f'Total cost is {total_price}\n'
    message += f'User : {order.user.id}'

    from django.template.loader import render_to_string

    html_message = render_to_string('order_email_template.html', {
        'order_id': order_id,
        'order_products': [
            {
                'product': order_product.product,
                'number_of_days': order_product.rental_period_length(),
                'product_cost': order_product.product.price * order_product.rental_period_length(),
                'insurance_cost': total_insurance_cost,  # Apply total insurance cost uniformly
                'total_item_cost': total_item_cost,
            }
            for order_product in order.order_products.all()
        ],
        'user_id': order.user.id,
        'total_insurance_cost': total_insurance_cost,  # Include total insurance cost
        'total_price': total_price,
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

