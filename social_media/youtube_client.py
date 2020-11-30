import logging
import googleapiclient.discovery

from django.utils import timezone
from django.conf import settings
from social_media.constants import YOUTUBE_DATE_FORMAT

logger = logging.getLogger(__name__)


class YoutubeAPIException(Exception):
    pass


class YoutubeAPIAdapter:

    @staticmethod
    def modify_data(data):
        modified_data = []
        for video in data:
            snippet = video['snippet']
            modified_data.append({'title': snippet['title'], 'published_at': snippet['publishedAt'],
                                  'description': snippet['description'], 'thumbnails': snippet['thumbnails'],
                                  'external_id': video['id']['videoId']})
        return modified_data


class YoutubeApiClient:
    api_service_name = 'youtube'
    api_version = 'v3'

    def __init__(self):
        self.youtube_service = googleapiclient.discovery.build(self.api_service_name, self.api_version,
                                                               developerKey=settings.YOUTUBE_API_KEY)

    def search_videos(self, query, start_date='', end_date=timezone.now().strftime(YOUTUBE_DATE_FORMAT)):
        if not start_date:
            raise YoutubeAPIException('start date missing')
        request = self.youtube_service.search().list(
            part='snippet',
            maxResults=50,
            q=query,
            order='date',
            publishedAfter=start_date,
            publishedBefore=end_date,
            type="video"
        )
        response = request.execute()
        return response


youtube_api_client = YoutubeApiClient()
