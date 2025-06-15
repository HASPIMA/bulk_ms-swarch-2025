from typing import Any

from pydantic import BaseModel

from models.message import MessageModel


class ProcessingModel(BaseModel):
    task_id: str
    message: MessageModel
    result: Any = None
