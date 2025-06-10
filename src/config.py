"""Configuration settings for the application."""

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(case_sensitive=True)

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000


settings = Settings()
