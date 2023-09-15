import logging

from enum import Enum
from pathlib import Path

from pydantic_settings import BaseSettings
from colorama import Fore


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]  # Путь к корню проекта


# Класс конфигурации приложения

class AppConfig(BaseSettings):    
    BOT_TOKEN: str
    ENV: str = "dev"

    class Config:
        extra='ignore'
        env_file = PROJECT_ROOT / ".env"


# Класс конфигурации БД PostgreSQL 

class PostgresConfig(BaseSettings):
    PG_DB: str = "serverstats_db"
    PG_USER: str = "user"
    PG_PASSWD: str = "passwd"
    PG_HOST: str = "localhost"
    PG_PORT: int = 5432

    class Config:
        extra='ignore'
        env_file = PROJECT_ROOT / ".env"


# Конфигурация логгера

class LoggingConfig(BaseSettings):
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Path = PROJECT_ROOT / "logs.log"
    LOG_FORMAT: str = (
        "[%(asctime)s]:"
        "[%(levelname)-8s]:"
        "[%(name)s]:"
        "[%(filename)s]:::"
        "%(message)s"
    )
    LOG_FORMAT_COLORS: str = (
        Fore.BLUE
        + "[%(asctime)s]:"
        + Fore.CYAN
        + "[%(levelname)-8s]:"
        + Fore.GREEN
        + "[%(name)s]:"
        + Fore.MAGENTA
        + "[%(filename)s]:::"
        + Fore.WHITE
        + "%(message)s"
    )

    class Config:
        extra='ignore'
        env_file = PROJECT_ROOT / ".env"



# Применение конфигурации логгера

def configure_logger():
    basic_formatter = logging.Formatter(LOG_CONF.LOG_FORMAT)
    colored_formatter = logging.Formatter(LOG_CONF.LOG_FORMAT_COLORS)

    file_handler = logging.FileHandler(LOG_CONF.LOG_FILE)
    file_handler.setFormatter(basic_formatter)

    std_handler = logging.StreamHandler()
    std_handler.setFormatter(colored_formatter)

    logger = logging.getLogger()
    logger.setLevel(LOG_CONF.LOG_LEVEL)
    logger.addHandler(file_handler)
    logger.addHandler(std_handler)


APP_CONF = AppConfig()
LOG_CONF = LoggingConfig()
POSTGRES_CONF = PostgresConfig()

configure_logger()
