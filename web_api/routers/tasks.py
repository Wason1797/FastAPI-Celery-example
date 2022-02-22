import json
from fastapi import APIRouter
from ..worker import celery


router = APIRouter()


@router.get("/check-task/{id}")
def check_task(id: str):
    task = celery.AsyncResult(id)

    error = json.loads(task.backend.get(task.backend.get_key_for_task(task.id)).decode('utf-8')) if task.state == 'FAILURE' else None
    if error:
        del error['children']
        del error['traceback']

    response = {
        'status': task.state,
        'result': task.result if task.state == 'SUCCESS' else None,
        'progress': task.info if task.state == 'PROGRESS' else None,
        'task_id': id,
        'error': error
    }

    return response
