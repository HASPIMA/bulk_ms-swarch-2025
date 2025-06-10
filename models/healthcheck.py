from pydantic import BaseModel
from typing import Literal


class HealthCheck(BaseModel):
    status: Literal["ok", "error"]
    message: str
    version: str
