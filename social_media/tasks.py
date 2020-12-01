import logging
from django.utils import timezone
from fam_pay.celery import app

from social_media.constants import YOUTUBE_SEARCH_QUERY
from social_media.models import VideoArchive
from social_media.youtube_client import YoutubeApiClient

logger = logging.getLogger(__name__)


@app.task()
def fetch_latest_videos():
    latest_video = VideoArchive.objects.order_by('-published_at').first()
    if not latest_video:
        start_date = timezone.now() - timezone.timedelta(days=4)
    else:
        start_date = latest_video.published_at
    end_date = timezone.now()
    video_data = YoutubeApiClient().fetch_videos(YOUTUBE_SEARCH_QUERY, start_date=start_date, end_date=end_date)
    for video in video_data:
        logger.info('creating video record wi external_id %s', video['external_id'])

        # check for duplicates, move this to model clean method
        if VideoArchive.objects.filter(external_id=video['external_id']).exists():
            logger.info('duplicate found for external_id %s', video['external_id'])
            continue
        VideoArchive.objects.create(**video)
