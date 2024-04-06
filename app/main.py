from fastapi import FastAPI

from app.config import settings
from app.containers import Container
from app.users.router import router as user_router
from app.exception_handlers import (
    register_error_handlers as register_global_error_handlers,
)


def create_app() -> FastAPI:
    _ = Container()
    application = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/docs",
        redoc_url="/re-docs",
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description="""
        The fastapi project template
        """,
    )

    # Register exception handlers
    register_global_error_handlers(app=application)

    # application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(user_router, prefix=settings.API_PREFIX)
    # application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = create_app()
