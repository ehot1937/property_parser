from peewee import BooleanField, CharField

from parser_app.postgres.models.base_pg_model import BasePGModel


class Marketing(BasePGModel):
    name = CharField(max_length=50, null=True)
    mail = CharField(max_length=50, unique=True, null=True)
    phone = CharField(max_length=50, unique=True, null=True)
    instagram = CharField(max_length=50, null=True)
    site = CharField(max_length=50, null=True)
    contacted = BooleanField(default=False)
    agreed = BooleanField(default=False)
    registred = BooleanField(default=False)
    type = CharField(max_length=50, null=True)
