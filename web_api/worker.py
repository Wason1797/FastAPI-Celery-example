import os
from celery import Celery

BROKER_URL = os.getenv('BROKER_URL')
BACKEND_URL = os.getenv('BACKEND_URL')

celery = Celery('celery', backend=BACKEND_URL, broker=BROKER_URL)
