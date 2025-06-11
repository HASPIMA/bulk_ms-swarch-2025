from os import getenv

from celery import Celery
from dotenv import load_dotenv

DEFAULT_REDIS_URL = 'redis://localhost:6379/0'

load_dotenv()

celery = Celery(__name__)
celery.conf.update(
    broker_url=getenv('CELERY_BROKER_URL', DEFAULT_REDIS_URL),
    result_backend=getenv('CELERY_RESULT_BACKEND', DEFAULT_REDIS_URL),
    include=[
        # Add the module containing the task
    ]
)
