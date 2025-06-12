from pydantic import UUID4, BaseModel


class Person(BaseModel):
    id: UUID4
    name: str
