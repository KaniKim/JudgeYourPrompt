import os
from pydantic_settings import BaseSettings

__all__ = ["settings", "check_db"]


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    tset: bool = False
    project_name: str = "Judge My Prompt"
    oauth_token_secret: str = "my_dev_secret"


from dotenv import load_dotenv

load_dotenv()

username = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")
port = os.environ.get("DB_PORT")

settings = Settings(
    database_url=f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
)

check_db = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
