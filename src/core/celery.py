from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('ecb_feed')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'rates_daily': {
        'task': 'api.tasks.get_exchange_rates',
        'schedule': crontab(hour=15, minute=5)
    }
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))