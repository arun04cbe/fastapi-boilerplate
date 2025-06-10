from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):

    model_config = SettingsConfigDict(case_sensitive=True)

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000


settings = Settings()