from fastapi import APIRouter

from .examples import router as example_router
from .tasks import router as tasks_router

router = APIRouter(
    tags=["API"],
)

router.include_router(
    tasks_router,
)

router.include_router(
    example_router,
)


__all__ = ["router"]
