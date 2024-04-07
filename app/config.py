import os

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="")

    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "FASTAPI-PROJECT-STRUCTURE")
    API_PREFIX: str = "/api/v1"
    LOGGING_CONFIG_FILE: str = os.path.join(BASE_DIR, "logging.yaml")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    SECRET_KEY: str = "test"


settings = Settings()
