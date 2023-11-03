import datetime
import logging
import sys

from peewee import PostgresqlDatabase
from peewee_migrate import Router

from parser_app.settings import db_settings

logger = logging.getLogger("peewee-migrate")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class Migrator:
    def __init__(self):
        self.DB_NAME = db_settings.pg_database

        self.router = Router(
            PostgresqlDatabase(
                database=db_settings.pg_database,
                user=db_settings.pg_user,
                password=db_settings.pg_password,
                host=db_settings.pg_host,
                port=db_settings.pg_port,
            ),
            migrate_dir="./parser_app/postgres/migrations",
            logger=logger,
        )

    def migrate(self):
        self.router.run()

    def create(self, migration_name: str):
        # path = Path.cwd()
        # path = path.joinpath("db/postgres")
        # auto = str(path)
        self.router.create(migration_name)


if __name__ == "__main__":
    migrator = Migrator()

    if sys.argv[1:]:
        argument = sys.argv[1:][0]
        if argument == "rollback":
            migrator.router.rollback()
            print("Rollback completed")
        else:
            migrator.create(argument + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M"))
            print("Migration created")
    else:
        migrator.migrate()
        print("Migration completed")
