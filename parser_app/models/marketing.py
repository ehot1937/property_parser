from parser_app.models.base_data_model import BaseDataModel


class Marketing(BaseDataModel):
    name: str | None = None
    mail: str | None = None
    phone: str | None = None
    instagram: str | None = None
    site: str | None = None
    contacted: bool | None = False
    agreed: bool | None = False
    registred: bool | None = False
    type: str | None = None
