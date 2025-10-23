from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str
    API_PREFIX: str = "/api"
    ALLOW_ORIGINS: List[str] = ["*"]

    ORION_HOST: str
    FIWARE_SERVICE: str
    FIWARE_SERVICEPATH: str

settings = Settings()
