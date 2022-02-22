from fastapi import APIRouter
from ..schemas.item import Item
from ..worker import celery

import socket

router = APIRouter()


@router.post('/')
def process_item(item: Item):
    task = celery.send_task('process_item.task', args=[item.dict()])
    current_ip = socket.gethostbyname(socket.gethostname())
    return dict(id=task.id, url=f'{current_ip}:5000/check-task/{task.id}')
