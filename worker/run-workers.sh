#!/bin/bash


celery -A worker worker --loglevel=info -n worker1@%h -O fair &
celery -A worker worker --loglevel=info -n worker2@%h -O fair
