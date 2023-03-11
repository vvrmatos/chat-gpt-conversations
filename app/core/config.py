import os
from pydantic import BaseSettings


class ChatGPTSettings(BaseSettings):
    API_KEY: str = os.getenv('OPENAI_KEY')
    MODEL: str = 'gpt-3.5-turbo'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


class DBSettings(BaseSettings):
    PROJECT_NAME: str = 'MongoDB'
    PROJECT_DESCRIPTION: str = 'Chat GPT Conversation'
    DEBUG_MODE: bool = False
    DATABASE_URL: str = 'mongodb://localhost:27017'
    DATABASE_NAME: str = 'chatgpt'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


gtp_settings = ChatGPTSettings()
db_settings = DBSettings()
