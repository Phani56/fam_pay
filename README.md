# fam_pay
fampay assignment

App to fetch and store data related to youtube videos in regular intervals(every 1 min). 
The data will be stored in a Postgres database and can be retrieved using an api.

Youtube API key 
* Add youtube api key to env variables with `export YOUTUBE_API_KEY="key_here"`

** Postgres and Redis(as a broker for celery) are required.

Installation
* create a new virtual env(py3) and activate it.
* Run `pip install -r requirements/base.txt`
* Run `python manage.py migrate`
* update local databse settings
* Run this command for the cron job `celery -A fam_pay worker -l info -B`
* Run the server `python manage.py runserver`

API endpoint
* Check the api at `http://localhost:8000/video-archive/`
* Search by passing `search` as query_param. Ex: `http://localhost:8000/video-archive/?search=england`


