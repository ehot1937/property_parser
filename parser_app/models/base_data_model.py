from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BaseDataModel(BaseModel):
    class Config:
        from_attributes = True

    id: UUID = None
    created_at: datetime = None
