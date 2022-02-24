# FastAPI-Celery-example

 An asynchronous backend example using celery, fastapi and docker

 The main goal of this project is to illustrate asynchronous backends, and to give an example on how to leverage python for time-consuming tasks.

## Tools and Framewors

- Celery
- RabbitMQ
- Redis
- FastAPI
- Flower

## The architecture

TBD

## How to run

Run `docker-compose up` and all the necesary components will be created.

- You can go to the example UI at `http://your-docker-host:80` here you can place tasks and see their progress

  - If for some reason your docker host is not in localhost, change [this line](https://github.com/Wason1797/FastAPI-Celery-example/blob/d46a2ad314311b58ea62738561e0bf93fb0623ae/ui/src/js/tasks.js#L5) so the ui points to the correct url

- You can check the celery workers status with flower at `http://your-docker-host:5555`

- You can check the API docs at `http://your-docker-host:5000/docs`
