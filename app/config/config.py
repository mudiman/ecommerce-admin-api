from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "Ecommerce Admin API"
    db_url: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str
    api_path: str = "/api/v1"
    low_stock_threshold: int
    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    return Settings()
