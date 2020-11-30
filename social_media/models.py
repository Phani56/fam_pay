from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class VideoArchive(models.Model):

    title = models.TextField(db_index=True)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField(db_index=True)
    thumbnails = JSONField(default=dict, blank=True, null=True)
    external_id = models.CharField(db_index=True, max_length=255, unique=True)  # video provider external id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
