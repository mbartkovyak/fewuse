import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fewuse.settings')

app = Celery('fewuse')

app.config_from_object('django.conf:settings', namespace='CELERY')
broker_connection_retry_on_startup = True


@app.task(bind=True)
def hello_world_task(self):
    print("Hello World!")

