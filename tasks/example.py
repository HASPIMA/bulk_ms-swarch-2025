
from celery import shared_task

from models.company import CompaniesResponse
from models.person import PeopleResponse
from services.example.companies import generate_companies
from services.example.people import generate_people


@shared_task(pydantic=True)
def companies_task() -> CompaniesResponse:
    '''
    Celery task to generate a list of companies.
    '''
    generated = generate_companies()

    return CompaniesResponse(
        companies=generated,
    )


@shared_task(pydantic=True)
def people_task() -> PeopleResponse:
    '''
    Celery task to generate a list of people.
    '''
    generated = generate_people()

    return PeopleResponse(
        people=generated,
    )
