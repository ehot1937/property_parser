from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    pg_host: str = "host_name"
    pg_port: int = 5432
    pg_user: str = "user_name"
    pg_password: str = "password"
    pg_database: str = "db-name"


db_settings = DbSettings()
