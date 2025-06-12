from pydantic import BaseModel, UUID4


class Person(BaseModel):
    id: UUID4
    name: str
