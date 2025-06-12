from contextlib import asynccontextmanager
from os import getenv

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from models.healthcheck import HealthCheck
from routers import router

# Load environment variables from .env file
load_dotenv()


__version__ = "0.0.0"


# NOTE: Implement lifespan before instanting the app
@asynccontextmanager
async def lifespan(app: FastAPI):
    '''
    Lifespan context manager to set up and tear down resources
    for the FastAPI application.
    This is where we can set up things like database connections,
    background tasks, etc.
    '''
    # Setup section
    print(f'Starting Celery setup')
    from worker import celery

    app.state.celery_app = celery
    print(f'Completed Celery setup')

    yield

    # Cleanup section


app = FastAPI(
    title="MeetUN Bulk Backend",
    description="API for bulk operations on MeetUN",
    version=__version__,
    lifespan=lifespan,
    # FIXME: Disable docs in production
)


origins = [
    # "http://localhost:3000",  # Local development

    # Production URLs
    # "https://example.com",

    # In case we need to allow everything
    # "*",
]

# Add middleware to set CORS headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add middleware to compress responses larger than 500 bytes
app.add_middleware(GZipMiddleware, minimum_size=500)


@app.get(
    "/",
)
async def read_root() -> HealthCheck:
    return HealthCheck(
        status="ok",
        message="MeetUN Bulk API is running",
        version=__version__,
    )

app.include_router(router, prefix="/api")


if __name__ == '__main__':
    import uvicorn

    # Get the port from the environment variables or use the default
    port = int(getenv("PORT", 8000))

    uvicorn.run(app, host="0.0.0.0", port=port)
