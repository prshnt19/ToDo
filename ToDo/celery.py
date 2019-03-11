from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

app = Celery('ToDo')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDo.settings')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'Asia/Kolkata'
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'home.tasks.send_mail',
        'schedule': crontab(minute=58, hour=22),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
