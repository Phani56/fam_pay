import logging
import googleapiclient.discovery

from django.conf import settings

logger = logging.getLogger(__name__)


class YoutubeApiClient:
    api_service_name = 'youtube'
    api_version = 'v3'

    def __init__(self):
        self.youtube_service = googleapiclient.discovery.build(self.api_service_name, self.api_version,
                                                               developerKey=settings.YOUTUBE_API_KEY)

    def search_videos(self, query, **kwargs):
        request = self.youtube_service.search().list(
            part='snippet',
            maxResults=200,
            q=query,
            order='date',
            publishedAfter='2020-09-28T00:00:00Z',
            publishedBefore='2020-01-31T00:00:00Z',
            type="video"
        )
        response = request.execute()
        return response
