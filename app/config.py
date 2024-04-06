import os


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "FASTAPI-PROJECT-STRUCTURE")
    API_PREFIX = "/api/v1"


settings = Settings()
