import uuid
from datetime import datetime

from peewee import DateTimeField, Model, UUIDField

from parser_app.postgres.database import get_database


class BasePGModel(Model):
    class Meta:
        database = get_database()

    id = UUIDField(primary_key=True, default=uuid.uuid4())
    created_at = DateTimeField(default=datetime.now())
