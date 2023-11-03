from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_user: str = "postgres"
    pg_password: str = "postgres"
    pg_database: str = "oh-parser"


db_settings = DbSettings()
