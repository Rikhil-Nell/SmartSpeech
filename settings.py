from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    groq_key: str = Field(..., validation_alias="GROQ_API_KEY")

    class Config:
        env_file = ".env"
