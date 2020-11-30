from . import common


class Settings(common.Settings):

    DEBUG = True

    YOUTUBE_API_KEY = 'AIzaSyDBnAddneEJDBQxV8jf68R0PYrsx0ABNYk'

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "fam_pay_assignment",
            "USER": "postgres",
            "PASSWORD": "postgres",
        }
    }
