from . import common
import os


class Settings(common.Settings):

    DEBUG = True

    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "fam_pay_assignment",
            "USER": "postgres",
            "PASSWORD": "postgres",
        }
    }
