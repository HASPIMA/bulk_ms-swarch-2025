from fastapi import APIRouter, status

from models.message import MessageModel
from models.processing import ProcessingModel
from tasks.examples import companies_task

router = APIRouter(
    prefix='/companies',
)


@router.get(
    '/',
    status_code=status.HTTP_202_ACCEPTED,
)
async def read_companies() -> ProcessingModel:
    '''
    Creates a task to generate a list of companies.
    '''

    task = companies_task.delay()  # type: ignore
    message = MessageModel(
        es='Procesando la lista de empresas',
        en='Processing companies list',
    )

    return ProcessingModel(
        task_id=task.id,
        message=message,
    )
