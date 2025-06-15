from celery.result import AsyncResult
from fastapi import APIRouter, status

from models.message import MessageModel
from models.processing import ProcessingModel

router = APIRouter(
    prefix='/tasks',
)


@router.get(
    '/status',
    summary='Get the status of the tasks',
    description='Returns the status of the tasks.',
    response_description='Status of the tasks',
    status_code=status.HTTP_200_OK,
)
async def get_tasks_status(
    task_id: str,
):
    '''
    Get the status of the tasks.
    '''
    task = AsyncResult(task_id)
    message: MessageModel
    result = None

    match task.state:
        case 'PENDING':
            message = MessageModel(
                es='Esperando la tarea',
                en='Waiting for the task',
            )
        case 'STARTED':
            message = MessageModel(
                es='Tarea iniciada',
                en='Task started',
            )
        case 'RETRY':
            message = MessageModel(
                es='Tarea reintentada',
                en='Task retried',
            )
        case 'FAILURE':
            message = MessageModel(
                es='Tarea fallida',
                en='Task failed',
            )
            # FIXME: Add information about the error
            # result = task.result
        case 'SUCCESS':
            message = MessageModel(
                es='Tarea exitosa',
                en='Task successful',
            )
            result = task.result
        case _:
            message = MessageModel(
                es='Estado desconocido',
                en='Unknown state',
            )
    return ProcessingModel(
        task_id=str(task.id),
        message=message,
        # FIXME: Fix the type of result (Any) to the correct type (List[PersonModel] or List[CompanyModel])
        result=result,
    )
