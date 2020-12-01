from celery.schedules import crontab
from django.conf import settings

broker_url = settings.BROKER_URL
accept_content = ['json']
timezone = 'UTC'

beat_schedule = {
        'fetch_video_data': {
            'task': 'fam_pay.social_media.tasks.fetch_latest_videos',
            'schedule': crontab(minute='*/1')
        }
    }
