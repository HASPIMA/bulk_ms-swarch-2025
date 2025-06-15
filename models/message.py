from pydantic import BaseModel


class MessageModel(BaseModel):
    es: str
    en: str
