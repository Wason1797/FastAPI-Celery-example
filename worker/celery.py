import os
from celery import Celery

BROKER_URL = os.getenv('BROKER_URL')
BACKEND_URL = os.getenv('BACKEND_URL')

app = Celery('celery', backend=BACKEND_URL, broker=BROKER_URL, include=['worker.tasks'])

if __name__ == '__main__':
    app.start()
