from django.apps import AppConfig


class LendloopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lendloop'

    def ready(self):
        from lendloop.signals import order_created