from social_media.models import VideoArchive
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class VideoArchiveSerializer(ModelSerializer):

    class Meta:
        model = VideoArchive
        exclude = ('updated_at', 'external_id')
