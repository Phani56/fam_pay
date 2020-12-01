import os
from celery import Celery
from django.conf import settings
from configurations import importer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')

importer.install()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')
app = Celery('fam_pay')

app.config_from_object('settings.celery_config')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

