import logging
import sys
from fastapi import FastAPI
import yaml

from app.config import settings
from app.containers import Container
from app.users.router import router as user_router
from app.exception_handlers import (
    register_error_handlers as register_global_error_handlers,
)


def setup_logger(config_file: str, default_level=logging.INFO) -> None:
    with open(config_file, mode="r", encoding="utf-8") as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception as e:
            print("Failed to load configuration file. Using default configs", e)
            logging.basicConfig(level=default_level, stream=sys.stdout)


def create_app() -> FastAPI:
    _ = Container()
    application = FastAPI(
        title=settings.project_name,
        docs_url="/docs",
        redoc_url="/re-docs",
        openapi_url=f"{settings.api_prefix}/openapi.json",
        description="""
        The fastapi project template
        """,
    )

    # Set logger
    setup_logger(config_file=settings.logging_config_file)

    # Register exception handlers
    register_global_error_handlers(app=application)

    # application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(user_router, prefix=settings.api_prefix)
    # application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = create_app()
