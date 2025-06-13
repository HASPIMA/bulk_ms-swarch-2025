from os import getenv

from celery import Celery
from dotenv import load_dotenv

DEFAULT_RESULT_BACKEND_URL = 'redis://localhost:6379/0'
DEFAULT_BROKER_URL = 'amqp://guest:guest@localhost:5672/'

load_dotenv()

celery = Celery(__name__)
celery.conf.update(
    broker_url=getenv('CELERY_BROKER_URL', DEFAULT_BROKER_URL),
    result_backend=getenv('CELERY_RESULT_BACKEND', DEFAULT_RESULT_BACKEND_URL),
    include=[
        # Add the module containing the task
        'tasks.examples',
    ]
)
