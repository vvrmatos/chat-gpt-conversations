from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MongoDB"
    PROJECT_DESCRIPTION: str = "Chat GPT Conversation"
    DEBUG_MODE: bool = False
    DATABASE_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "fastapi_example"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
