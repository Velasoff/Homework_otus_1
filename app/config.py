from logging.handlers import SYSLOG_UDP_PORT

import pydantic
from sqlalchemy.engine.url import URL


class Settings(pydantic.BaseSettings):
    SERVICE_NAME: str = "homework_otus"
    ROOT_PATH: str = "/"
    AUTH_HEADER: str = "Authorization"

    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    LOG_BODY: bool = False
    LOG_REQUEST_ID_HEADER: str = "X-SAT-Span-Id"
    LOG_EXCLUDED_PATHS: list = [".*/docs", ".*/openapi.json"]

    SYSLOG_HOST: str = "127.0.0.1"
    SYSLOG_PORT: int = SYSLOG_UDP_PORT

    DB_DRIVER: str = "postgresql"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "app_pswd"
    DB_DATABASE: str = "app_db"

    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 0
    DB_ECHO: bool = False

    @property
    def DB_DSN(self) -> URL:
        return URL.create(self.DB_DRIVER, self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_PORT, self.DB_DATABASE)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
