FROM python:3.8

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /celery/worker
WORKDIR /celery


ENTRYPOINT bash worker/run-workers.sh
