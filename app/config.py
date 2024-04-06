import os

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="")

    project_name: str = os.getenv("PROJECT_NAME", "FASTAPI-PROJECT-STRUCTURE")
    api_prefix: str = "/api/v1"
    logging_config_file: str = os.path.join(BASE_DIR, "logging.yaml")


settings = Settings()
