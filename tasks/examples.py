
from celery import shared_task

from models.examples.company import CompaniesResponse
from models.examples.person import PeopleResponse
from services.examples.companies import generate_companies
from services.examples.people import generate_people


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
