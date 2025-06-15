from fastapi import APIRouter

from .companies import router as companies_router
from .people import router as people_router

router = APIRouter(
    prefix='/examples',
)


router.include_router(
    companies_router,
)

router.include_router(
    people_router,
)

__all__ = ['router']
