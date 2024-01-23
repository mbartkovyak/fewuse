from fewuse.celery import app
from telegram.client import send_message
from lendloop.models import Product
@app.task(bind=True)
def product_created_task(self, product_id):
    product = (
        Product.objects.select_related("category")
        .prefetch_related("tags")
        .select_related("location")
        .prefetch_related("rankings")
        .select_related("user")
        .get(id=product_id)
    )

    message = f"Product {product_id} created!\n"

    send_message(message)