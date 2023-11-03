import logging
import uuid

from peewee import ModelSelect, PostgresqlDatabase

from parser_app.models.base_data_model import BaseDataModel
from parser_app.models.marketing import Marketing
from parser_app.postgres.models.base_pg_model import BasePGModel
from parser_app.postgres.models.marketing import Marketing as PGMarketing

logger = logging.getLogger(__name__)


class MarketingConnector:
    """
    Abstract class for exchanging data with database PostgreSQL

    _model: model which represents application entity
    _db_model: model which represents Peewee database entity
    """

    _model: BaseDataModel = Marketing
    _db_model: BasePGModel = PGMarketing

    def __init__(self, database: PostgresqlDatabase):
        self._database = database

    def to_pydantic_objects(self, db_objects: list | ModelSelect) -> list:
        """Converts Peewee model objects to Pydantic objects"""

        result = []
        for db_object in db_objects:
            result.append(self._model.from_orm(db_object))

        return result

    def get(self, *args) -> list[BaseDataModel] | None:
        """Returns pydantic models with filters"""

        db_objects = self._db_model.select()

        if not db_objects:
            return None

        return self.to_pydantic_objects(db_objects)

    def save(self, model_object: BaseDataModel) -> BaseDataModel:
        """Creates the application pydantic model in the database"""

        model_data = model_object.model_dump()
        model_data["id"] = uuid.uuid4()
        model_data.pop("created_at")

        model_data = {
            key: value for key, value in model_data.items() if not isinstance(value, dict)
        }

        logger.info(str(model_data))

        db_object = self._db_model.create(**model_data)
        model_object.id = db_object.id
        model_object.created_at = db_object.created_at
        return model_object
