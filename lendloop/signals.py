from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from lendloop.models import Order
from lendloop.tasks import order_created_task

@receiver(post_save, sender=Order)
def order_created(sender, instance, **kwargs):
    order_created_task.apply_async(args =(instance.id,), countdown = 5)