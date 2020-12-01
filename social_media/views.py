
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import SearchFilter

from social_media.models import VideoArchive
from social_media.serializers import VideoArchiveSerializer

# Create your views here.


class VideoArchiveViewSet(GenericViewSet, ListModelMixin):

    model = VideoArchive
    serializer_class = VideoArchiveSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('title', 'description')

    def get_queryset(self):
        return VideoArchive.objects.all()
