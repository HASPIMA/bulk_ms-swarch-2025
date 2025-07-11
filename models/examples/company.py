from pydantic import UUID4, BaseModel


class Company(BaseModel):
    id: UUID4
    name: str


class CompaniesResponse(BaseModel):
    companies: list[Company]
