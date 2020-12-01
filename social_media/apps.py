from django.apps import AppConfig


class SocialMediaConfig(AppConfig):
    name = 'social_media'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import tasks
