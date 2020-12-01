import logging

import googleapiclient.discovery
from django.conf import settings
from django.utils import timezone

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

    def fetch_videos(self, query, start_date='', end_date=timezone.now()):
        video_data = []
        if not start_date:
            raise YoutubeAPIException('start date missing')

        if (end_date - start_date).days > 30:
            # added this check for local testing purpose
            raise YoutubeAPIException('interval too big')

        kwargs = {'part': 'snippet', 'maxResults': 50, 'q': query, 'order': 'date',
                  'publishedAfter': start_date.strftime(YOUTUBE_DATE_FORMAT),
                  'publishedBefore': end_date.strftime(YOUTUBE_DATE_FORMAT), 'type': 'video'}

        while True:
            print ('in loop')
            request = self.youtube_service.search().list(**kwargs)
            response = request.execute()
            video_data.extend(response['items'])
            if len(response['items']) < 50:
                break
            kwargs['pageToken'] = response['nextPageToken']
        return YoutubeAPIAdapter.modify_data(video_data)

