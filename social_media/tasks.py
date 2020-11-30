from django.utils import timezone

from social_media.constants import YOUTUBE_DATE_FORMAT, YOUTUBE_SEARCH_QUERY
from social_media.models import VideoArchive
from social_media.youtube_client import youtube_api_client


def fetch_latest_videos():
    latest_video = VideoArchive.objects.order_by('-published_at').first()
    if not latest_video:
        return
    end_date = timezone.now().strftime(YOUTUBE_DATE_FORMAT)
    start_date = latest_video.published_at.strftime(YOUTUBE_DATE_FORMAT)
    video_data = youtube_api_client.search_videos(YOUTUBE_SEARCH_QUERY, start_date=start_date, end_date=end_date)
