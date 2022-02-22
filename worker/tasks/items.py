
import traceback
from time import sleep

from ..celery import app
from ..common.constants import StatusConstants


@app.task(name='process_item.task', bind=True)
def process_item(self, item):
    try:
        for i in range(30):
            sleep(1)
            self.update_state(state=StatusConstants.PROGRESS, meta={'done': i, 'total': 30})
        return {"result": f"Processed item {item.get('name')}"}
    except RuntimeError as ex:
        self.update_state(
            state=StatusConstants.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n')
            })
        raise ex
