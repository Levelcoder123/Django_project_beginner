import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bms.settings')

app = Celery('bms')

# for enable our asia/karachi timezone
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Karachi')

app.config_from_object('django.conf:settings', namespace='CELERY')

# celery beat settings...

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
