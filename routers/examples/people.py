from uuid import uuid4

from fastapi import APIRouter, status

from models.message import MessageModel
from models.processing import ProcessingModel
from tasks.examples import people_task

router = APIRouter(
    prefix='/people',
)


@router.get(
    '/',
    status_code=status.HTTP_202_ACCEPTED,
)
async def read_people() -> ProcessingModel:
    '''
    Creates a task to generate a list of people.
    '''

    task = people_task.delay()  # type: ignore
    message = MessageModel(
        es='Procesando la lista de personas',
        en='Processing people list',
    )

    return ProcessingModel(
        task_id=task.id,
        message=message,
    )
