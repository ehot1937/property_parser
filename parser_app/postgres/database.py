from peewee import PostgresqlDatabase

from parser_app.settings import db_settings

_database = None


def get_database() -> PostgresqlDatabase:
    global _database

    if not _database:
        _database = PostgresqlDatabase(
            database=db_settings.pg_database,
            user=db_settings.pg_user,
            password=db_settings.pg_password,
            host=db_settings.pg_host,
            port=db_settings.pg_port,
        )

    return _database
